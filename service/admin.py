from django.contrib import admin
from .models import ServiceType, ServiceVendor


class ServiceTypeAdmin(admin.ModelAdmin):
    fields = ['name', 'price']
    list_display = ['name', 'price']


class ServiceVendorAdmin(admin.ModelAdmin):
    fields = ['name', 'cost_installation', 'cost_monthly']
    list_display = ['name', 'cost_installation', 'cost_monthly']


admin.site.register(ServiceType, ServiceTypeAdmin)
admin.site.register(ServiceVendor, ServiceVendorAdmin)
