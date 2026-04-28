from django.contrib import admin
from django.urls import path, include
from user import views

urlpatterns = [
    path('index/', views.gretting, name='index'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),

]