from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Profile
from images.models import Post

def signup(request):
    if request.method == 'POST':
        if request.POST['username'] and request.POST['password'] and request.POST['password2']:
            if request.POST['password'] == request.POST['password2']:
                try:
                    user = User.objects.get(username=request.POST['username'])
                    return render(request, 'accounts/signup.html', {'error':'Username has already been taken :('})
                except User.DoesNotExist:
                    user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
                    user_profile = Profile()
                    user_profile.user = user
                    user_profile.save()
                    auth.login(request, user)
                    return redirect('home')
            else:
                return render(request, 'accounts/signup.html', {'error':'Passwords must match :('})
        else:
            return render(request, 'accounts/signup.html', {'error':'All fields must be filled :('})
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        if request.POST['username'] and request.POST['password']:
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                return render(request, 'accounts/login.html', {'error': 'Password or username is incorrect'})
        else:
            return render(request, 'accounts/login.html', {'error': 'Failed login'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    else:
        return render(request, 'accounts/login.html', {'error': 'Some technical flaw, sorry for that :('})

@login_required(login_url='/crossroad')
def user_showcase(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        profile = Profile.objects.get(user=user)
        posts = Post.objects.filter(publisher=user_id)
        return render(request, 'accounts/user_showcase.html', {'user':user, 'profile': profile, 'posts':posts})
    except User.DoesNotExist:
        return redirect('home')