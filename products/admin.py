from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'main_genre',
        'sub_genre',
        'price',
        'image',
    )

    ordering = ('main_genre', 'title')


admin.site.register(Product, ProductAdmin)
