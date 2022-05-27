from django.contrib import admin
from .models import BackOne
from django import forms
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class BackOneResource(resources.ModelResource):
    class Meta:
        model = BackOne
        fields = (
            'id', 'name', 'ipaddress', 'serial_number', 'sid',
            'address', 'geolocation', 'contact__name', 'contact__phone',
            'connection_status__name', 'connection_type__name',
            'service_type__name', 'service_type__price',
            'service_vendor__name', 'service_vendor__cost_installation', 'service_vendor__cost_monthly',
            'description'
        )
        export_order = (
            'id', 'name', 'ipaddress', 'serial_number', 'sid',
            'address', 'geolocation', 'contact__name', 'contact__phone',
            'connection_status__name', 'connection_type__name',
            'service_type__name', 'service_type__price',
            'service_vendor__name', 'service_vendor__cost_installation', 'service_vendor__cost_monthly',
            'description'
        )


class BackOneAdminForm(forms.ModelForm):
    class Meta:
        model = BackOne
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput
        }


class BackOneAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {
          'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    }
    form = BackOneAdminForm
    fields = ['name', 'ipaddress', 'serial_number', 'sid',
              'connection_status', 'connection_type',
              'service_type', 'service_vendor', 'contact',
              'address', 'geolocation',
              'description', 'orbit',
              'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    list_display = ['name', 'sid', 'address', 'connection_type', 'connection_status',
                    'service_type', 'service_price',
                    'service_vendor', 'cost_installation', 'cost_monthly']
    list_filter = ('name', 'sid')
    list_per_page = 25
    resource_class = BackOneResource

    @staticmethod
    def service_price(obj):
        if obj.service_type == None:
            return None

        return obj.service_type.price

    @staticmethod
    def cost_installation(obj):
        if obj.service_vendor == None:
            return None
        return obj.service_vendor.cost_installation

    @staticmethod
    def cost_monthly(obj):
        if obj.service_vendor == None:
            return None
        return obj.service_vendor.cost_monthly




admin.site.register(BackOne, BackOneAdmin)

