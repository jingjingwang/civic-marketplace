from django.shortcuts import render, redirect
from django.contrib.messages import error
from django.contrib.auth.models import User
from .models import Job, Involve
from django.contrib.auth.decorators import login_required

def get_user_by_id(request):
    try:
        user = User.objects.get(id= request.user.id)
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

@login_required(login_url='/account/')
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
    released_jobs = []  
    # taking all the remaining jobs for now
    for job in Job.objects.all():
        if job not in user_jobs:
            recommended_jobs.append(job)
        if job.publisher == user:
            released_jobs.append(job)
    return render(request, 'dashboard/index.html', { 
        'user':user, 'user_jobs':user_jobs, 'recommended_jobs':recommended_jobs, 'released_jobs':released_jobs, 
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
        'user':user, 'job':job, 'publisher':job.publisher.username
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

def addjob(request):
    user = get_user_by_id(request)
    if user is None: return redirect('account:index')
    if request.method == 'GET':
        return render(request, 'dashboard/addjob.html', {'user':user})
    job = Job(title=request.POST['title'], description=request.POST['description'], publisher=user)
    job.save()
    return redirect('dashboard:index')

def profile(request):
    user = get_user_by_id(request)
    if user is None: return redirect('account:index')
    return render(request, 'dashboard/profile.html', {'user':user})

