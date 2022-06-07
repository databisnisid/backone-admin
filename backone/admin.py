from django.contrib import admin
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
from .models import BackOne
from project.models import Project, Po
from django import forms
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class BackOneResource(resources.ModelResource):
    class Meta:
        model = BackOne
        fields = (
            'id', 'name', 'ipaddress', 'ipaddress_local', 'serial_number', 'sid',
            'address', 'geolocation', 'contact__name', 'contact__phone',
            'connection_status__name', 'connection_type__name',
            'service_type__name', 'service_type__price',
            'service_vendor__name', 'service_vendor__cost_installation', 'service_vendor__cost_monthly',
            'project__name', 'po_number__number', 'baso__name',
            'description'
        )
        export_order = (
            'id', 'name', 'ipaddress', 'ipaddress_local', 'serial_number', 'sid',
            'address', 'geolocation', 'contact__name', 'contact__phone',
            'connection_status__name', 'connection_type__name',
            'service_type__name', 'service_type__price',
            'service_vendor__name', 'service_vendor__cost_installation', 'service_vendor__cost_monthly',
            'project__name', 'po_number__number', 'baso__name',
            'description'
        )


class BackOneAdminForm(forms.ModelForm):

    class Meta:
        model = BackOne
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'size': 50
            }),
            'password': forms.PasswordInput,
            'sid': forms.TextInput(attrs={
                'placeholder': 'Masukkan SID',
                'size': 30
            }
            ),
            'serial_number': forms.TextInput(attrs={
                'placeholder': 'Masukkan Serial Number',
                'size': 30
            }
            ),
            'backone_id': forms.TextInput(attrs={
                'placeholder': 'Masukkan BackOne Id Device',
                'size': 50
            }
            ),
            'backone_network': forms.TextInput(attrs={
                'placeholder': 'Masukkan BackOne Id Network',
                'size': 50
            }
            ),
        }

    def clean(self):
        po_number = self.cleaned_data['po_number']
        project = self.cleaned_data['project']

        if po_number is not None:
            try:
                po_id = Po.objects.get(id=po_number.id)
                if project != po_id.project:
                    raise ValidationError(
                        {'po_number': [_('Po Number is NOT matched with Project')]}
                    )
            except ObjectDoesNotExist:
                raise ValidationError(
                    {'po_number': [_('Po Number is Invalid')]}
                )


class BackOneAdmin(ImportExportModelAdmin, admin.ModelAdmin):
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

    #form = BackOneAdminForm

    fieldsets = (
        (None, {
            'fields': ('name', 'contact', 'geolocation', 'address', 'description')
        }),
        ('Project', {
            'classes': ('collapse',),
            'fields': ('project', 'po_number'),
        }),
        ('Technical', {
            'classes': ('collapse',),
            'fields': ('ipaddress', 'ipaddress_local',
                       'backone_id', 'backone_network'),
        }),
        ('SID & SN', {
            'classes': ('collapse',),
            'fields': ('sid', 'serial_number'),
        }),
        ('Connection', {
            'classes': ('collapse',),
            'fields': ('connection_type', 'connection_status'),
        }),
        ('Service', {
            'classes': ('collapse',),
            'fields': ('service_type', 'service_vendor'),
        }),
        ('Baso', {
            'classes': ('collapse',),
            'fields': ('baso',),
        }),
        ('Additional', {
            'classes': ('collapse',),
            'fields': ('orbit',),
        }),
    )

    #fields = ['__all__']
    """
    fields = ['name', 'ipaddress', 'serial_number', 'sid',
              'connection_status', 'connection_type',
              'service_type', 'service_vendor', 'contact',
              'geolocation', 'address',
              'project', 'po_number',
              'description', 'orbit',
              'created_at', 'updated_at',
              ]
    """
    exclude = ['username', 'password',]
    readonly_fields = ['created_at', 'updated_at']
    list_display = ['name', 'sid', 'address', 'connection_type', 'connection_status',
                    'service_type', 'service_price',
                    'service_vendor', 'cost_installation', 'cost_monthly',
                    'project', 'po_number', 'baso'
                    ]
    #list_filter = ('name', 'sid')
    search_fields = ('name', 'ipaddress', 'sid', 'project__name', 'po_number__number',
                     'address', 'connection_type__name', 'connection_status__name',
                     'backone_id', 'backone_network',
                     'service_vendor__name', 'service_type__name', 'baso__name')
    list_per_page = 25
    resource_class = BackOneResource

    @staticmethod
    def service_price(obj):
        if obj.service_type is None:
            return None

        return obj.service_type.price

    @staticmethod
    def cost_installation(obj):
        if obj.service_vendor is None:
            return None
        return obj.service_vendor.cost_installation

    @staticmethod
    def cost_monthly(obj):
        if obj.service_vendor is None:
            return None
        return obj.service_vendor.cost_monthly


admin.site.register(BackOne, BackOneAdmin)
