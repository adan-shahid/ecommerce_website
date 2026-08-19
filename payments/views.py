from django.shortcuts import render, redirect
from django.http import HttpResponse
from cart.models import CartItem, Cart
from orders.models import Order, OrderItem
import stripe
from django.contrib.auth.decorators import login_required

# Create your views here.
def payment(request):

    cart_items = CartItem.objects.filter(cart__user = request.user)
    print(cart_items)
    if not cart_items.exists():
        return redirect('product')

    return HttpResponse('This is for payments page')

def create_checkout_session(request):
    try:
        user_cart = request.user.cart

    except Cart.DoesNotExist:
        return redirect('cart_details')

    if not user_cart.items.exists():
        return redirect('product')

    order = Order.objects.create(
        user = request.user,
        total_price = user_cart.total_price,
        status = 'Pending'
    )


    line_items = []
    for item in user_cart.items.all():
        OrderItem.objects.create(
            order=order,
            product=item.product,
            price=item.product.price,
            quantity=item.quantity
        )

        line_items.append({
            'price_data': {
                'currency': 'pkr',
                'product_data':{
                    'name': item.product.name,
                },
                'unit_amount': int(item.product.price * 100),
            },
            'quantity': item.quantity,
        })

    print("ORDER ")
    print("Order ID:", order.id)
    print("User:", order.user)
    print("Total price:", order.total_price)
    print("Status:", order.status)

    print("\nORDER ITEMS ")
    for order_item in order.items.all():
        print(
            "Product:", order_item.product.name,
            "| Price:", order_item.price,
            "| Quantity:", order_item.quantity
        )

    print("\nSTRIPE LINE ITEMS ")
    print(line_items)
    

