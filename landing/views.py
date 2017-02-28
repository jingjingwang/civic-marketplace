from django.shortcuts import render
from django.contrib.auth.models import User

from dashboard.models import Job

def index(request):
    jobs = Job.objects.all()
    if request.user.is_authenticated:
        user = request.user
    else: user = None
    return render(request, 'landing/index.html', {'jobs':jobs, 'user':  user})
