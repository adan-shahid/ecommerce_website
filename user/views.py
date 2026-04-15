from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm
from django.contrib.auth import login


# Create your views here.

def gretting(request):
    return render(request, 'index.html')

def register_user(request):
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request,user)
        return redirect('greeting')
    context = {
        'form':form,
    }
    return render(request, 'register.html', context)