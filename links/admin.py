from django.contrib import admin

from links.models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'link', 'name', 'email', 'country', 'city', 'street', 'house_number',)
    list_filter = ('link', 'country',)
