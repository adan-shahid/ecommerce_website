from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('<int:order_id>/', views.order_detail, name='order_detail'),
    
]
