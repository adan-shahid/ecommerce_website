from django.contrib import admin
from django.urls import path, include
from products import views

urlpatterns = [
    path('', views.product_View, name='product'),
    path('product-detail/<int:product_id>/', views.product_detail, name='product-detail'),


]