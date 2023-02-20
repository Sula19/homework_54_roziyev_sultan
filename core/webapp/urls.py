from django.urls import path
from webapp.views.add_category import add_category
from webapp.views.add_product import add_product
from webapp.views.bonus import categories, delete, update
from webapp.views.product_view import product_view
from webapp.views.products_view import view

urlpatterns = [
    path('', view, name='view'),
    path('products/', view, name='view'),
    path('products/<int:pk>', product_view, name='product_view'),
    path('categories/', categories, name='categories'),
    path('products/add/', add_product, name='add_product'),
    path('categories/add', add_category, name='add_category'),
    path('delete/<int:pk>', delete, name='delete'),
    path('categories/<int:pk>/edit/', update, name='update')
]
