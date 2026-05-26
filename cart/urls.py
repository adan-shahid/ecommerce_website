from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('page/', views.cart, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name = 'add-to-cart'),
]
