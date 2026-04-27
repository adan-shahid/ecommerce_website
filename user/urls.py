from django.contrib import admin
from django.urls import path, include
from user import views

urlpatterns = [
    path('home/', views.gretting, name='home'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),  

]