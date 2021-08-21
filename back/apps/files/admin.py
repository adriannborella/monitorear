from django.contrib import admin
from .models import Files


@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    # readonly_fields = ('days_until_update_admin', )
    ordering = ['name']
    search_fields = ['name']
    list_display = ['name', 'path', 'last_date_update', 'last_date_info', 'days_until_update_admin']
    filter_fields = ['last_date_update']

    @admin.display(empty_value='???')
    def days_until_update_admin(self, obj):
        value = obj.days_until_update
        return f'{value} days'

    days_until_update_admin.allow_tags = True