from django.shortcuts import render, redirect
from django.contrib.messages import error
from django.contrib.auth.models import User
from django import forms
from .models import Job, Involve, Cause, Skill, JobCause, JobSkill
from account.models import UserCause, UserSkill, UserIdentity
from mimetypes import guess_extension
import random
import tempfile

def get_user_by_id(request):
    if 'user_id' not in request.session:
        error(request, 'Your session has expired.')
        return None
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

def index(request):
    user = get_user_by_id(request)
    if user is None: return redirect('account:index')
    user_jobs = []
    try:
        involves = Involve.objects.filter(participant=user.id)
        for involve in involves:
            user_jobs.append(Job.objects.get(id=involve.job.id))
    except (KeyError, Involve.DoesNotExist, Job.DoesNotExist):
        pass
    recommended_jobs = []  
    # taking all the remaining jobs for now
    for job in Job.objects.all():
        if job not in user_jobs:
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
        'user':user, 'user_jobs':user_jobs, 'recommended_jobs':[j[0] for j in recommended_jobs],
    })

def managejobs(request):
    user = get_user_by_id(request)
    if user is None: return redirect('account:index')
    released_jobs = Job.objects.filter(publisher=user)  
    return render(request, 'dashboard/managejobs.html', { 
        'user':user, 'released_jobs':released_jobs, 
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
        'skills':Skill.objects.all(), 'causes':Cause.objects.all()
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
    participated = len(get_involve(job, user)) > 0
    return render(request, 'dashboard/jobdetail.html', {
        'action': 'Unparticipate' if participated else 'Participate',
        'user':user, 'job':job, 'skills':Skill.objects.filter(jobskill__job=job), 'causes':Cause.objects.filter(jobcause__job=job),
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

class UploadFileForm(forms.Form):
    file = forms.FileField()

def handle_uploaded_file(fname, f):
    with open('dashboard/static/%s' % fname, 'wb+') as img:
        try:
            for chunk in f.chunks():
                img.write(chunk)
        finally:
            img.close()
    return img.name

def addjob(request):
    user = get_user_by_id(request)
    if user is None: return redirect('account:index')
    causes = Cause.objects.all()
    skills = Skill.objects.all()
    user_identities = [str(user.username)] + [str(ui.identity) for ui in UserIdentity.objects.filter(user=user)]
    if request.method == 'GET':
        return render(request, 'dashboard/addjob.html', {'user':user, 'causes':causes, 'skills':skills, 'user_identities':user_identities})
    if 'job_id' in request.POST:
        job = Job.objects.get(id=request.POST['job_id'])
    else:
        img = 'landing/img/portfolio-%d.jpg' % random.randint(1, 4)
        job = Job(title=request.POST['title'], description=request.POST['description'], publisher=user,
              identity=request.POST['identity'], location=request.POST['location'], time=request.POST['time'], thumb=img)
        job.save()
    if 'cover' in request.FILES and len(request.FILES['cover']) > 0:
        img = 'dashboard/img/jobs/job_cover_%d%s' % (job.id, guess_extension(request.FILES['cover'].content_type))
        handle_uploaded_file(img, request.FILES['cover'])
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
    return render(request, 'dashboard/profile.html', {'user':user, 'causes':causes, 'user_causes':user_causes, 'skills':skills, 'user_skills':user_skills, 'user_identities':user_identities})

