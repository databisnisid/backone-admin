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
    fields = ['name', 'ipaddress', 'serial_number', 'sid_number',
              'address', 'geolocation',
              'description', 'orbit',
              'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    list_display = ['name', 'ipaddress', 'address', 'sid_number', 'orbit']
    list_filter = ('name', 'ipaddress',)


admin.site.register(BackOne, BackOneAdmin)

