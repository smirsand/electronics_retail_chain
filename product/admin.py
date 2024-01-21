from django.contrib import admin

from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model', 'quantity', 'price', 'owner_link', 'hierarchy', 'city', 'country', 'release_date',)
    list_filter = ('name', 'owner_link', 'city', 'country',)
    readonly_fields = ('hierarchy', 'city', 'country', 'owner_link',)
