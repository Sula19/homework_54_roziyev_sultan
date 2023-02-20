from django.contrib import admin
from webapp.models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'category']
    list_filter = ['id', 'title', 'created_at']
    search_fields = ['title', 'category']
    fields = ['title', 'description', 'category', 'created_at', 'price']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    list_filter = ['id', 'title']
    fields = ['title', 'description']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
