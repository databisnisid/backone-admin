from django.contrib import admin
from .models import BackOne
from django import forms
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
import json


class BackOneAdminForm(forms.ModelForm):
    class Meta:
        model = BackOne
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput
        }


class BackOneAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {
          'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    }
    form = BackOneAdminForm
    fields = ['name', 'ipaddress', 'serial_number', 'sid',
              'connection_status', 'connection_type',
              'service_type',
              'address', 'geolocation',
              'description', 'orbit',
              'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    list_display = ['name', 'ipaddress', 'sid', 'address', 'connection_type', 'connection_status', 'service_type']
    list_filter = ('name', 'ipaddress')
    list_per_page = 25


admin.site.register(BackOne, BackOneAdmin)

