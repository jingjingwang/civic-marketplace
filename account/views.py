from django.shortcuts import render, redirect
from django.contrib.messages import error, success
from django.contrib.auth import authenticate,login,logout
from .models import User, Cause, Skill, UserIdentity, Organization, UserCause, UserSkill, PreferredTime, UserPreferredTime
from mimetypes import guess_extension
from google.cloud import storage

def login_view(request):
    if request.method == 'GET':
        #if request.user.is_authenticated:
        #return redirect('dashboard:index')
        return render(request, 'account/login.html')
    #user = authenticate(username=request.POST['username'], password=request.POST['password'])
    try:
        user = User.objects.get(username=request.POST['username'])
    except (KeyError, User.DoesNotExist):
        error(request, 'A user with this username does not exist.')        
        return redirect('account:login_view')
    if not user.check_password(request.POST['password']):
        error(request, 'Invalid password.')
        return redirect('account:login_view')
    request.session['user_id'] = user.id
    return redirect('dashboard:profile')

    #if user is not None:
    #    return redirect('dashboard:index')

def logout_view(request):
    logout(request)
    return redirect('landing:index')

def register(request):
    if request.method == 'GET':
        return render(request, 'account/register.html')
    if 'username' not in request.POST or len(request.POST['username']) < 3:
        error(request, 'Username must contain at least 3 characters.')
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
        user = User(username=request.POST['username'])
        user.set_password(request.POST['password'])
        user.save()
        #user = authenticate(username=request.POST['username'], password=request.POST['password'])
        #login(request, user)
        #return redirect('dashboard:index')
        request.session['user_id'] = user.id
        request.session.set_expiry(600)
        return redirect('dashboard:profile')
    else:
        error(request, 'This username has been registered.')
        return redirect('account:register')

def handle_uploaded_file(f, user_id):
    content_type = guess_extension(f.content_type)
    filename = 'users_avatar/%d%s' % (user_id, content_type)
    bucket = storage.Client().get_bucket('catalyst-market.appspot.com')
    blob = bucket.get_blob(filename)
    if blob is None: blob = bucket.blob(filename)
    for chunk in f.chunks():
        blob.upload_from_string(chunk)
    return blob.public_url

def change(request):
    if 'user_id' not in request.session:
        error(request, 'Invalid user.')
        return redirect('dashboard:profile')
    user = User.objects.get(id=request.session['user_id'])
    if 'username' not in request.POST or len(request.POST['username']) < 3:
        error(request, 'Username must contain at least 3 characters.')
        return redirect('dashboard:profile')
    if 'password' in request.POST and len(request.POST['password']) > 0:
        if len(request.POST['password']) < 6:
            error(request, 'Password must contain at least 6 characters.')
            return redirect('dashboard:profile')
        if 'confirm-password' not in request.POST or request.POST['password'] != request.POST['confirm-password']:
            error(request, 'Passwords do not match.')
            return redirect('dashboard:profile')
        user.set_password(request.POST['password'])
    if 'avatar' in request.FILES and len(request.FILES['avatar']) > 0:
        img = handle_uploaded_file(request.FILES['avatar'], user.id)
        user.avatar = img
    user.email = request.POST['email']
    user.save()
    UserCause.objects.filter(user=user).delete()
    for name in request.POST.getlist('causes'):
        cause = Cause.objects.get(name=name)
        user_cause = UserCause(user=user, cause=cause)
        user_cause.save()
    UserSkill.objects.filter(user=user).delete()
    for name in request.POST.getlist('skills'):
        skill = Skill.objects.get(name=name)
        user_skill = UserSkill(user=user, skill=skill)
        user_skill.save()
    UserPreferredTime.objects.filter(user=user).delete()
    for name in request.POST.getlist('preferred_times'):
        time = PreferredTime.objects.get(name=name)
        user_preferred_time = UserPreferredTime(user=user, preferred_time=time)
        user_preferred_time.save()
    identity = request.POST['identity'].strip()
    if len(identity) > 0:
        try:
            org = Organization.objects.get(name=identity)
        except (KeyError, Organization.DoesNotExist):
            error(request, 'Identity does not exist.')
            return redirect('dashboard:profile')
        user_identity = UserIdentity(user=user, identity=org)
        user_identity.save()
    success(request, 'Your changes have been saved.')
    return redirect('dashboard:profile')

