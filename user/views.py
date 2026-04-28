from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from django.contrib.auth import login, logout
from .forms import customUserCreationForm

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


def logout_view(request):
    logout(request)
    messages.info(request, 'You are logged out')
    return redirect('index')