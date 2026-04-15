from django.contrib import admin
from django.urls import path, include
from user import views

urlpatterns = [
    path('greeting/', views.gretting, name='greeting'),
    path('register/', views.register_user, name='register'),
]