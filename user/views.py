from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegistrationForm


# Create your views here.

def gretting(request):
    return render(request, 'index.html')

