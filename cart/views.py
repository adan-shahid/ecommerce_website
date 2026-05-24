from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product

# Create your views here.
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id = product_id)
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)

    if product_id_str in cart:
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1   

    request.session['cart'] = cart
    request.session.modifed = True
    return redirect('index')