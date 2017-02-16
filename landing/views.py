from django.shortcuts import render
from dashboard.models import Job

from account.models import User

def index(request):
    jobs = Job.objects.all()
    if 'user_id' in request.session:
        user = User.objects.get(id=request.session['user_id'])
    else: user = None
    return render(request, 'landing/index.html', {'jobs':jobs, 'user':user})
