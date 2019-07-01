from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'list_day', 'is_published', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', 'is_published')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'state', 'zip_code', 'price')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
