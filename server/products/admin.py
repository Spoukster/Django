from django.contrib import admin
from django.template.loader import render_to_string

from .models import Product, Category


class ProductsAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'picture', 'category',
        'cost', 'modified', 'created',
        'is_pure'
    ]

    list_filter = [
        'category', 'modified', 'created'
    ]

    search_fields = [
        'name', 'description'
    ]

    fieldsets = (
        (
            'Base', {
                'fields': ('name', 'category')
            },
        ),
        (
            'Content', {
                'fields': ('image', 'description', 'cost')
            },
        ),
    )

    def picture(self, obj):
        return render_to_string(
            'products/components/picture.html',
            {
                'image': obj.image
            }
        )


    def is_pure(self, obj):
        return obj.modified == obj.created


class ProductInline(admin.TabularInline):
    model = Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]

    search_fields = [
        'name', 'description'
    ]

    inlines = [
        ProductInline
    ]

admin.site.register(Product, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)
