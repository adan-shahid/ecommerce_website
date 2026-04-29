from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from django.contrib.auth import login, logout, authenticate
from .forms import customUserCreationForm, customUserChangeForm

# Create your views here.

def gretting(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = customUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success('Your account is created successfully.')
            return redirect('home')
    else:
        form = customUserCreationForm()
        
    context = {
        'form':form
        }
    return render(request, 'user/signup.html', context)

def login_view(request):
    if request.user.is_authenticated:
        messages.error(request,'You are already logged in')
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'you are logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Login credentials')
            return redirect('login')
               

    return render(request, 'user/login.html')





def logout_view(request):
    logout(request)
    messages.info(request, 'You are logged out')
    return redirect('index')