from django.contrib import admin

from purchase.models import Purchase


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_cost', 'quantity', 'supplier', 'buyer', 'data', 'hierarchy')
    list_filter = ('product_name',)
    readonly_fields = ('hierarchy',)
