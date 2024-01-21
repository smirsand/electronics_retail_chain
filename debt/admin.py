from django.contrib import admin

from debt.models import Debt


@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_id', 'product', 'borrower', 'debtor', 'duty', 'owner',)
    list_filter = ('borrower', 'debtor', 'duty',)
    # readonly_fields = ('product_id', 'product', 'borrower', 'debtor', 'duty',)
