from django.contrib import admin
from .models import ServiceType


class ServiceTypeAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'cost_installation', 'cost_monthly']
    list_display = ['name', 'price', 'cost_installation', 'cost_monthly']


admin.site.register(ServiceType, ServiceTypeAdmin)
