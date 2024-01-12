from django.contrib import admin

from links.models import Factory, Retail, IE


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'street', 'house_number',)
    list_filter = ('country',)
    # readonly_fields = ('level',)


@admin.register(Retail)
class RetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'street', 'house_number',)
    list_filter = ('country',)
    # readonly_fields = ('level',)


@admin.register(IE)
class IEAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'street', 'house_number',)
    list_filter = ('country',)
    # readonly_fields = ('level',)
