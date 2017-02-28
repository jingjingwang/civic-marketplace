from django.shortcuts import render, redirect
from django.contrib.messages import error, success
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def login_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('dashboard:index')
        return render(request, 'account/login.html')
    
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('dashboard:index')

    error(request, 'A user with this username does not exist.')
    return redirect('account:login_view')    
    

def logout_view(request):
    logout(request)
    return redirect('landing:index')

def register(request):
    if request.method == 'GET':
        return render(request, 'account/register.html')
    if 'username' not in request.POST or len(request.POST['username']) < 3:
        error(request, 'Username must contain at least 3 characters.')
        return redirect('account:register')
    if 'email' not in request.POST or len(request.POST['email']) < 3 or '@' not in request.POST['email']:
        error(request, 'Please enter a valid email.')
        return redirect('account:register')
    if 'password' not in request.POST or len(request.POST['password']) < 6:
        error(request, 'Password must contain at least 6 characters.')
        return redirect('account:register')
    if 'confirm-password' not in request.POST or request.POST['password'] != request.POST['confirm-password']:
        error(request, 'Passwords do not match.')
        return redirect('account:register')
    try:
        user = User.objects.get(username=request.POST['username'])
    except (KeyError, User.DoesNotExist):
        print ("got registration request")
        user = User(username=request.POST['username'], email=request.POST['email'])
        user.set_password(request.POST['password'])
        user.save()
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        login(request, user)
        print ("Log in success after registering.")
        return redirect('dashboard:index')
        request.session.set_expiry(600)
        return redirect('dashboard:index')
    else:
        error(request, 'This username has been registered.')
        return redirect('account:register')

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
    user.set_password(request.POST['password'])
    user.save()
    success(request, 'Your changes have been saved.')
    return redirect('dashboard:profile')

