from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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

def remove_cart_item(request, item_id):
    print('This function is triggered')
    cart_item = get_object_or_404(CartItem, id=item_id)
    print(f"Current User: {request.user}")
    print(f"Cart Owner: {cart_item.cart.user}")
    if cart_item.cart.user == request.user:
        print("WARNING: User matches! continuing deletion.")
        cart_item.delete()

        messages.success(request, 'This Cart item is removed successfully!')
    else:
        print("WARNING: User mismatch! Skipping deletion.")
        messages.error(request, 'You are unauthorized to remove this item from cart')

    return redirect('index')


def update_cart_item(request, item_id):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        cart_item = get_object_or_404(CartItem, id=item_id)
        cart_item.quantity = quantity
        cart_item.save()
    return redirect('cart-detail')