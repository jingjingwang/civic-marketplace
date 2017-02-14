from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from django.contrib.messages import error, success

from .models import Job, Involve
from login.models import User

def index(request, user_id):
    jobs = []
    try:
        involves = Involve.objects.filter(participant=user_id)
        for involve in involves:
            jobs.append(Job.objects.get(id=involve.job.id))
    except (KeyError, Involve.DoesNotExist, Job.DoesNotExist):
        pass
    alljobs = Job.objects.all()
    return render(request, 'dashboard/index.html', {
        'message':'Hello ' + str(user_id), 'part_list':jobs, 'user_id':user_id, 'job_list':alljobs
    })

def jobdetail(request, job_id):
    user_id = request.GET.get('user_id')
    try:
        job = Job.objects.get(id=job_id)
    except (KeyError, Job.DoesNotExist):
        #error(request, 'The job does not exist.')
        return HttpResponse('dashboard:index')
    return render(request, 'dashboard/jobdetail.html', {
        'title': job.title, 'description': job.description, 'user_id': user_id, 'job_id': job_id
    })

def participate(request):
    if request.method == 'GET':
        return redirect('dashboard:index')
    user = User.objects.get(id=request.POST['user_id'])
    job = Job.objects.get(id=request.POST['job_id'])
    participate = Involve.objects.filter(job=job, participant=user)
    if len(participate) == 0:
        participate = Involve(job=job, participant=user)
        participate.save()
        #success(request, 'Successfully added.')
        return redirect('dashboard:index', user_id=request.POST['user_id'])
    #error(request, 'Already participated.')
    return redirect('dashboard:index', user_id=request.POST['user_id'])

def addjob(request):
    if request.method == 'GET':
        return redirect('dashboard:index')
    user = User.objects.get(id=request.POST['user_id'])
    job = Job(title=request.POST['title'], description=request.POST['description'], publisher=user)
    job.save()
    #success(request, 'Successfully added.')
    return redirect('dashboard:index', user_id=request.POST['user_id'])
