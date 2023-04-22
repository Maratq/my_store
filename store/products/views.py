from django.shortcuts import render

from products.models import ProductCategory, Product


def index(request):
    return render(request, 'products/index.html', context={
        'title': 'My store',

    })


def products(request):
    return render(request, 'products/products.html', context={
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    })
