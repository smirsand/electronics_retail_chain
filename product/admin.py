from django.contrib import admin

from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'model', 'release_date', 'manufacturer',)
    list_filter = ('product_name', 'release_date',)
