from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order
# Create your views here.
@login_required
def order_list(request):
    orders = Order.objects.filter(user= request.user)
    context = {
        'orders':orders,
    }
    return render(request, 'orders/order_list.html', context)

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id= order_id, user=request.user)
    context = {
        'order':order,
    }
    return render(request, 'orders/order_detail.html', context)