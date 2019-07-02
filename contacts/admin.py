from django.contrib import admin
from .models import Contacts


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing_title', 'email', 'contact_date')
    list_display_links = ('id', 'name', 'listing_title')
    list_filter = ('name',)
    search_fields = ('name', 'listing_title', 'email'),
    list_per_page = 25


admin.site.register(Contacts, ContactAdmin)
