from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('page/', views.cart, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name = 'add-to-cart'),
    path('cart-detail', views.cart_detail, name = 'cart-detail'),

    path('remove-cart-item/<int:item_id>/', views.remove_item_cart, name = 'remove-cart-item'),

]
