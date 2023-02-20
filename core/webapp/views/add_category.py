from django.shortcuts import redirect, render
from django.core.handlers.wsgi import WSGIRequest
from webapp.models import Category


def add_category(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'add_category.html')
    category_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description')
    }
    Category.objects.create(**category_data)
    return redirect('/')
