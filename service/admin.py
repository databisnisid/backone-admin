from django.contrib import admin
from .models import ServiceType


class ServiceTypeAdmin(admin.ModelAdmin):
    fields = ['name', 'price']
    list_display = ['name', 'price']


admin.site.register(ServiceType, ServiceTypeAdmin)
