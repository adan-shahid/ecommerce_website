from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from cart.models import CartItem, Cart
from orders.models import Order, OrderItem
import stripe
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.urls import reverse

stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.
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

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        client_reference_id=str(order.id),
        success_url=request.build_absolute_uri(reverse('payment_success')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('payment_cancel')),
    )

    return redirect(checkout_session.url, code=303)


def payment_success(request):
    session_id = request.GET.get('session_id')
    if not session_id:
        return redirect('cart_detail')

    # here i am retrieving transaction details from Stripe
    session = stripe.checkout.Session.retrieve(session_id)
    order_id = session.client_reference_id
    order = get_object_or_404(Order, id=order_id, user=request.user)

    # now i update the order status and save stripe payment id
    order.status = 'Paid'
    order.transaction_id = session.payment_intent
    order.save()

    request.user.cart.items.all().delete()
    context = {
        'order':order,
    }

    return render(request, 'payments/payment_success.html', context)

def payment_cancel(request):
    return render(request, 'payments/payment_cancel.html')
