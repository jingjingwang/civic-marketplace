from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.messages import error, success
from .models import User

def index(request):
    if 'user_id' in request.session:
        return redirect('dashboard:index')
    return render(request, 'account/index.html')

def login(request):
    if request.method == 'GET':
        return redirect('account:index')
    try:
        user = User.objects.get(email=request.POST['email'])
    except (KeyError, User.DoesNotExist):
        error(request, 'A user with this email does not exist.')
        return redirect('account:index')
    if request.POST['password'] != user.password:
        error(request, 'Invalid password.')
        return redirect('account:index')
    request.session['user_id'] = user.id
    return redirect('dashboard:index')

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('landing:index')

def register(request):
    if 'username' not in request.POST or len(request.POST['username']) < 3:
        error(request, 'Username must contain at least 3 characters.')
        return redirect('account:index')
    if 'email' not in request.POST or len(request.POST['email']) < 3 or '@' not in request.POST['email']:
        error(request, 'Please enter a valid email.')
        return redirect('account:index')
    if 'password' not in request.POST or len(request.POST['password']) < 6:
        error(request, 'Password must contain at least 6 characters.')
        return redirect('account:index')
    if 'confirm-password' not in request.POST or request.POST['password'] != request.POST['confirm-password']:
        error(request, 'Passwords do not match.')
        return redirect('account:index')
    try:
        user = User.objects.get(email=request.POST['email'])
    except (KeyError, User.DoesNotExist):
        user = User(email=request.POST['email'], display_name=request.POST['username'], password=request.POST['password'])
        user.save()
        request.session['user_id'] = user.id
        return redirect('dashboard:index')
    else:
        error(request, 'This email has been registered.')
        return redirect('account:index')

def change(request):
    if 'username' not in request.POST or len(request.POST['username']) < 3:
        error(request, 'Username must contain at least 3 characters.')
        return redirect('dashboard:profile')
    if 'email' not in request.POST or len(request.POST['email']) < 3 or '@' not in request.POST['email']:
        error(request, 'Please enter a valid email.')
        return redirect('dashboard:profile')
    if 'password' not in request.POST or len(request.POST['password']) < 6:
        error(request, 'Password must contain at least 6 characters.')
        return redirect('dashboard:profile')
    if 'confirm-password' not in request.POST or request.POST['password'] != request.POST['confirm-password']:
        error(request, 'Passwords do not match.')
        return redirect('dashboard:profile')
    if 'user_id' not in request.session:
        error(request, 'Invalid user.')
        return redirect('dashboard:profile')
    user = User.objects.get(id=request.session['user_id'])
    user.email = request.POST['email']
    user.password = request.POST['password']
    user.save()
    success(request, 'Your changes have been saved.')
    return redirect('dashboard:profile')
