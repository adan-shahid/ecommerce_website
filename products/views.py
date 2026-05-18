from django.shortcuts import render
from .models import Product
# Create your views here.

def product_View(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'product/product.html', context)


def product_detail(request):
    return render(request, 'product/product_detail.html')