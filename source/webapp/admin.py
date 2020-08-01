from django.contrib import admin
from .models import Guest


class GuestAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = ('pk', 'name', 'email', 'text', 'status', 'create_at', 'update_at')
    list_display_links = ('pk', 'name')
    search_fields = ('name',)


admin.site.register(Guest, GuestAdmin)
