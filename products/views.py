from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.

def product_View(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'product/product.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product':product,
    }
    return render(request, 'product/product_detail.html', context)