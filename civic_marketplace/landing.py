from django.shortcuts import render
from django.contrib.auth.models import User

from dashboard.models import Job

def index(request):
    jobs = Job.objects.all()
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
    else: user = None
    return render(request, 'landing.html', {'jobs':jobs, 'user':user})
