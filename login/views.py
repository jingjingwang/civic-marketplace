from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.messages import error, success
from .models import User

def index(request):
    return render(request, 'login/index.html')

def login(request):
    if request.method == 'GET':
        return redirect('login:index')
    try:
        user = User.objects.get(email=request.POST['email'])
    except (KeyError, User.DoesNotExist):
        error(request, 'A user with this email does not exist.')
        return redirect('login:index')
    if request.POST['password'] != user.password:
        error(request, 'Invalid password.')
        return redirect('login:index')
    success(request, 'Hello ' + user.display_name)
    return redirect('dashboard:index', user_id=user.id)

def register(request):
    if request.method == 'GET':
        return redirect('login:index')
    if request.POST['password'] != request.POST['confirm-password']:
        error(request, 'The confirmation password does not match the password you first entered.')
        return redirect('login:index')
    try:
        user = User.objects.get(email=request.POST['email'])
    except (KeyError, User.DoesNotExist):
        user = User(email=request.POST['email'], display_name=request.POST['username'], password=request.POST['password'])
        user.save()
        success(request, 'Successfully registered.')
        return redirect('login:index')
    else:
        error(request, 'This email has been registered.')
        return redirect('login:index')
