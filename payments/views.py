from django.shortcuts import render, redirect
from django.http import HttpResponse
from cart.models import CartItem, Cart

# Create your views here.
def payment(request):

    cart_items = CartItem.objects.filter(cart__user = request.user)
    print(cart_items)
    if not cart_items.exists():
        return redirect('product')

    return HttpResponse('This is for payments page')