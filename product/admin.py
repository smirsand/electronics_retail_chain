from django.contrib import admin

from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'quantity', 'price', 'supplier', 'owner', 'hierarchy', 'release_date',)
    list_filter = ('name', 'release_date',)
    readonly_fields = ('hierarchy',)
