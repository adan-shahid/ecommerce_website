from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import login


# Create your views here.

def gretting(request):
    return render(request, 'index.html')
