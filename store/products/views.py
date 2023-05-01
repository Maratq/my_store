from django.shortcuts import render
from products.models import ProductCategory, Product, Basket
from users.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def index(request):
    return render(request, 'products/index.html', context={
        'title': 'My store',

    })


def products(request, category_id=None, page_number=1):
    products = Product.objects.filter(category=category_id) if category_id else Product.objects.all()
    per_page = 3
    paginator = Paginator(products,per_page)
    products_paginator = paginator.page(page_number)

    return render(request, 'products/products.html', context={
        'title': 'Store - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': products_paginator,
    })


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
