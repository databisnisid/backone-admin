from django.contrib import admin
from .models import MyCompany, OtherCompany
from django_google_maps import fields as map_fields
from django_google_maps import widgets as map_widgets
from django import forms


class MyCompanyAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {
          'widget': map_widgets.GoogleMapsAddressWidget(attrs={
              'data-map-type': 'roadmap',
              'placeholder': 'Masukkan alamat dan tekan enter',
              'size': 200
          })
        },
        map_fields.GeoLocationField: {
            'widget': forms.TextInput(attrs={
                'readonly': 'readonly',
                'size': 50
            })
        },
    }
    list_display = ['name', 'code']
    exclude = ['created_at', 'updated_at']

    class Meta:
        model = MyCompany


class OtherCompanyAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {
          'widget': map_widgets.GoogleMapsAddressWidget(attrs={
              'data-map-type': 'roadmap',
              'placeholder': 'Masukkan alamat dan tekan enter',
              'size': 200
          })
        },
        map_fields.GeoLocationField: {
            'widget': forms.TextInput(attrs={
                'readonly': 'readonly',
                'size': 50
            })
        },
    }
    list_display = ['name', 'code']
    exclude = ['created_at', 'updated_at']

    class Meta:
        model = OtherCompany


#admin.site.register(MyCompany, MyCompanyAdmin)
#admin.site.register(OtherCompany, OtherCompanyAdmin)
