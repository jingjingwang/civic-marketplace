from django.shortcuts import render, redirect
from django.contrib.messages import error, success
from django.db.models import Avg
from django import forms
from mimetypes import guess_extension
from google.cloud import storage
from django.contrib.auth.decorators import login_required
from datetimewidget.widgets import DateTimeWidget
import random

from .models import Job, Involve, JobCause, JobSkill, JobForm
from account.models import User, UserIdentity, Cause, Skill, UserCause, UserSkill, PreferredTime, UserPreferredTime

def get_user_by_id(request):
    try:
        user = User.objects.get(id=request.session['user_id'])
    except (KeyError, User.DoesNotExist):
        error(request, 'User does not exist.')
        return None
    return user

def get_job_by_id(request):
    if 'job_id' not in request.session:
        error(request, 'Job does not exist.')
        return None
    try:
        job = Job.objects.get(id=request.session['job_id'])
    except (KeyError, Job.DoesNotExist):
        error(request, 'Job does not exist.')
        return None
    return job

def get_involve(job, user):
    return Involve.objects.filter(job=job, participant=user)

#@login_required(login_url='/account/')
def index(request):
    user = get_user_by_id(request)
    if user is None: return redirect('account:index')
    past_jobs = []
    current_jobs = []
    involves = Involve.objects.filter(participant=user.id)
    for involve in involves:
        job = Job.objects.get(id=involve.job.id)
        if job.past: past_jobs.append(job)
        else: current_jobs.append(job)

    recommended_jobs = []  
    for job in Job.objects.filter(past=False):
        if job not in past_jobs and job not in current_jobs:
            w_cause = w_skill = 0
            causes = Cause.objects.filter(usercause__user=user)
            for jobcause in JobCause.objects.filter(job=job):
                if jobcause.cause in causes: w_cause += 1
            skills = Skill.objects.filter(userskill__user=user)
            for jobskill in JobSkill.objects.filter(job=job):
                if jobskill.skill in skills: w_skill += 1
            recommended_jobs.append((job, w_cause + w_skill))
    recommended_jobs.sort(key=lambda x: x[1], reverse=True)
     
    return render(request, 'dashboard/index.html', { 
        'user':user, 'past_jobs':past_jobs, 'current_jobs':current_jobs,
        'recommended_jobs':[j[0] for j in recommended_jobs],
    })

def managejobs(request):
    user = get_user_by_id(request)
    if user is None: return redirect('account:index')
    upcoming_jobs = Job.objects.filter(publisher=user, past=False)  
    past_jobs = Job.objects.filter(publisher=user, past=True)
    return render(request, 'dashboard/managejobs.html', { 
        'user':user, 'upcoming_jobs':upcoming_jobs, 'past_jobs':past_jobs
    })

def manage_one_job(request, job_id):
    user = get_user_by_id(request)
    if user is None: return redirect('account:index')
    try:
        job = Job.objects.get(id=job_id)
    except (KeyError, Job.DoesNotExist):
        error(request, 'The job does not exist.')
        return redirect('dashboard:index')
    request.session['job_id'] = job_id
    return render(request, 'dashboard/manage_one_job.html', {
        'user':user, 'job':job, 'job_skills':Skill.objects.filter(jobskill__job=job), 'job_causes':Cause.objects.filter(jobcause__job=job),
        'skills':Skill.objects.all(), 'causes':Cause.objects.all(),
        'involved_users':User.objects.filter(involve__job=job),
        'job_form':JobForm(instance=job)
    })

def jobdetail(request, job_id):
    user = get_user_by_id(request)
    if user is None: return redirect('account:index')
    # For now allowing every job to be seen, add a check if it's not true
    try:
        job = Job.objects.get(id=job_id)
    except (KeyError, Job.DoesNotExist):
        error(request, 'The job does not exist.')
        return redirect('dashboard:index')
    request.session['job_id'] = job_id
    try:
        involve = Involve.objects.get(job=job, participant=user)
    except (KeyError, Involve.DoesNotExist):
        involve = None
    other_users = User.objects.filter(involve__job=job)[:10]
    for other_user in other_users:
        t = Involve.objects.filter(participant=user).aggregate(Avg('score'))['score__avg']
        #if t is None: other_user.score = 0
        #else: other_user.score = int(t)
        #TODO: filter None
        other_user.score = int(5)
    return render(request, 'dashboard/jobdetail.html', {
        'involve':involve, 'user':user, 'job':job, 'skills':Skill.objects.filter(jobskill__job=job), 'causes':Cause.objects.filter(jobcause__job=job),
        'other_users':other_users
    })

def participate(request):
    if request.method == 'GET':
        return redirect('dashboard:index')
    user = get_user_by_id(request)
    if user is None: return redirect('account:index')
    job = get_job_by_id(request)
    if job is None: return redirect('account:index')
    del request.session['job_id']
    participate = get_involve(job, user)
    if len(participate) == 0:
        participate = Involve(job=job, participant=user)
        participate.save()
        return redirect('dashboard:index')
    else:
        participate[0].delete()
        return redirect('dashboard:index')

def handle_uploaded_file(f, job_id):
    content_type = guess_extension(f.content_type)
    filename = 'job_cover_%d%s' % (job_id, content_type)
    client = storage.Client()
    bucket = client.get_bucket('catalyst-market.appspot.com')
    blob = bucket.get_blob('jobs_cover_img/' + filename)
    if blob is None: blob = bucket.blob('jobs_cover_img/' + filename)
    for chunk in f.chunks():
        blob.upload_from_string(chunk)
    return blob.public_url

def addjob(request):
    user = get_user_by_id(request)
    if user is None: return redirect('account:index')
    causes = Cause.objects.all()
    skills = Skill.objects.all()
    user_identities = [str(user.username)] + [str(ui.identity) for ui in UserIdentity.objects.filter(user=user)]
    if request.method == 'GET':
        return render(request, 'dashboard/addjob.html', {'user':user, 'causes':causes, 'skills':skills, 'user_identities':user_identities, 'job_form':JobForm()})
    if 'job_id' in request.POST:
        job = JobForm(request.POST, instance=Job.objects.get(id=request.POST['job_id']))
    else:
        job = JobForm(request.POST)
    if job.is_valid():
        job = job.save()
    else:
        error(request, job.errors)
        return redirect('dashboard:managejobs')
    if 'cover' in request.FILES and len(request.FILES['cover']) > 0:
        print request.FILES['cover']
        img = handle_uploaded_file(request.FILES['cover'], job.id)
    else:
        img = 'landing/img/portfolio-%d.jpg' % random.randint(1, 4)
    job.thumb = img
    job.save()

    JobSkill.objects.filter(job=job).delete()
    for skill in request.POST.getlist('skills'):
        jobskill = JobSkill(job=job, skill=Skill.objects.get(name=skill))
        jobskill.save()
    JobCause.objects.filter(job=job).delete()
    for cause in request.POST.getlist('causes'):
        jobcause = JobCause(job=job, cause=Cause.objects.get(name=cause))
        jobcause.save()
    return redirect('dashboard:managejobs')

def profile(request):
    user = get_user_by_id(request)
    if user is None: return redirect('account:index')
    causes = Cause.objects.all()
    user_causes = causes.filter(usercause__user=user)
    skills = Skill.objects.all()
    user_skills = skills.filter(userskill__user=user)
    user_identities = UserIdentity.objects.filter(user=user)
    return render(request, 'dashboard/profile.html', {
        'user':user, 'causes':causes, 'user_causes':user_causes, 'skills':skills, 'user_skills':user_skills, 'user_identities':user_identities,
        'preferred_times':PreferredTime.objects.all(),
        'user_preferred_times':PreferredTime.objects.filter(userpreferredtime__user=user)
    })

def public_profile(request, user_id):
    user = User.objects.get(id=user_id)
    causes = Cause.objects.filter(usercause__user=user)
    skills = Skill.objects.filter(userskill__user=user)
    involves = Involve.objects.filter(participant=user)
    return render(request, 'dashboard/public_profile.html', {'user':user, 'skills':skills, 'causes':causes, 'involves':involves})

def review(request):
    if request.method == 'GET':
        user = User.objects.get(id=request.GET['user_id'])
        job = Job.objects.get(id=request.GET['job_id'])
        involve = Involve.objects.get(participant=user, job=job)
        return render(request, 'dashboard/review.html', {'user':user, 'job':job, 'involve':involve})
    user = User.objects.get(id=request.POST['user_id'])
    job = Job.objects.get(id=request.POST['job_id'])
    involve = Involve.objects.get(participant=user, job=job)
    involve.review = request.POST['review']
    involve.score = request.POST['score']
    involve.save()
    return redirect('dashboard:manage_one_job', request.POST['job_id'])
