from django.shortcuts import render, get_object_or_404, redirect
from django.core.handlers.wsgi import WSGIRequest
from webapp.models import Category, Product


def add_product(request: WSGIRequest):
    if request.method == 'GET':
        category = Category.objects.all()
        return render(request, 'add_product.html', context={'categories': category})
    product_data = {
        'title': request.POST.get('title'),
        'price': request.POST.get('price'),
        'image': request.POST.get('image'),
        'category': get_object_or_404(Category, title=request.POST.get('category')),
        'description': request.POST.get('description')
    }
    Product.objects.create(**product_data)
    return redirect('/')
