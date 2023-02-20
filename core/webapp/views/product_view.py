from django.shortcuts import render, get_object_or_404
from django.core.handlers.wsgi import WSGIRequest
from webapp.models import Product


def product_view(request: WSGIRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'product_view.html', context=context)
