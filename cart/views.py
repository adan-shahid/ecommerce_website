from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required

# Create your views here.

def cart(request):
    return render(request, 'cart/cart_page.html' )

def cart_detail(request):
    cart_items = CartItem.objects.filter(cart__user=request.user)
    cart_total = 0
    for item in cart_items:
        subtotal = item.product.price * item.quantity
        cart_total += subtotal

    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
    }
    
    return render(request, 'cart/cart_details.html', context)

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart, created = Cart.objects.get_or_create(user=request.user) #find the user cart, or create one if they don't have.
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    print(f'added {product.name} to cart database')
    return redirect('index')
