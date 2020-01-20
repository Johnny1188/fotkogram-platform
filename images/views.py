from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url="/crossroad")
def home(request):
    return render(request, 'images/home.html')

def crossroad(request):
    return render(request, 'images/crossroad.html')
