from django.contrib import admin

from purchase.models import Purchase


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'quantity', 'supplier', 'buyer', 'data', 'owner',)
    list_filter = ('product_name',)
