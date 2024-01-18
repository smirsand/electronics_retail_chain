from django.contrib import admin

from debt.models import Debt


@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):
    list_display = ('borrower', 'debtor', 'duty',)
    list_filter = ('borrower', 'debtor', 'duty',)
