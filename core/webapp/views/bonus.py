from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from webapp.models import Category


def categories(request: WSGIRequest):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'categories.html', context=context)


def delete(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('categories')


def update(request: WSGIRequest, pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'update_category.html', context={'category': category})
    category.title = request.POST.get('title')
    category.description = request.POST.get('description')
    category.save()
    return redirect('categories')
