from django.shortcuts import render
from webapp.models import Product
from django.core.handlers.wsgi import WSGIRequest


def view(request: WSGIRequest):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'home.html', context=context)
