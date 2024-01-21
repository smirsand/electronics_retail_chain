from django.contrib import admin

from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model', 'quantity', 'price', 'supplier', 'owner_link', 'hierarchy', 'release_date',)
    list_filter = ('name', 'supplier', 'owner_link',)
    readonly_fields = ('hierarchy',)
