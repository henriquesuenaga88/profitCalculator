from django.shortcuts import render
from .models import Product


def product_list(request):
    products = Product.objects.all()
    context = {
       'product_list': products
    }
    return render(request, 'product/list.html', context)
