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
from connector.utils import run_command
from django.shortcuts import render
#from import_export.admin import ImportExportActionModelAdmin


class BackOneResource(resources.ModelResource):
    class Meta:
        model = BackOne
        fields = (
            'id', 'name', 'ipaddress', 'ipaddress_local', 'serial_number', 'sid',
            'address', 'geolocation', 'contact__name', 'contact__phone',
            'connection_status__name', 'connection_type__name',
            'service_type__name', 'service_type__price',
            'service_vendor__name', 'service_vendor__cost_installation', 'service_vendor__cost_monthly',
            'project__name', 'po_number__number', 'baso__name', 'baso__date',
            'description'
        )
        export_order = (
            'id', 'name', 'ipaddress', 'ipaddress_local', 'serial_number', 'sid',
            'address', 'geolocation', 'contact__name', 'contact__phone',
            'connection_status__name', 'connection_type__name',
            'service_type__name', 'service_type__price',
            'service_vendor__name', 'service_vendor__cost_installation', 'service_vendor__cost_monthly',
            'project__name', 'po_number__number', 'baso__name', 'baso__date',
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
            'fields': ('is_priority', 'name', 'contact', 'geolocation', 'address', 'description')
        }),
        ('Project', {
            'classes': ('collapse',),
            'fields': ('project', 'po_number', 'po_number_vendor'),
        }),
        ('Data Teknis', {
            'classes': ('collapse',),
            'fields': ('ipaddress', 'ipaddress_local',
                       'backone_id', 'backone_network',
                       'ping_status',),
        }),
        ('SID & SN', {
            'classes': ('collapse',),
            'fields': ('sid', 'serial_number'),
        }),
        ('Koneksi', {
            'classes': ('collapse',),
            'fields': ('connection_type', 'connection_status'),
        }),
        ('Layanan', {
            'classes': ('collapse',),
            'fields': ('service_type', 'service_vendor'),
        }),
        ('Baso', {
            'classes': ('collapse',),
            'fields': ('baso', 'baso_date'),
        }),
        #('Additional', {
        #    'classes': ('collapse',),
        #    'fields': ('orbit',),
        #}),
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
    readonly_fields = ['created_at', 'updated_at', 'is_priority', 'baso_date']
    list_display = ['name', 'sid', 'ipaddress', 'address',
                    'po_number', 'po_number_vendor', 'project',
                    'connection_type', 'connection_status',
                    'service_type', 'service_vendor',
                    'baso', 'baso_date', 'description', 'is_priority'
                    ]
    list_filter = ('is_priority',)
    search_fields = ('name', 'ipaddress', 'sid', 'project__name', 'po_number__number',
                     'address', 'connection_type__name', 'connection_status__name',
                     'backone_id', 'backone_network',
                     'service_vendor__name', 'service_type__name', 'baso__name')
    list_per_page = 25
    actions = ['check_ifconfig', 'check_firewall', 'check_dns', 'check_routing',
               'check_backone_status',
               'activate_backone_ab_wan_lan0', 'deactivate_backone_local_conf']
    resource_class = BackOneResource

    def get_actions(self, request):
        actions = super(BackOneAdmin, self).get_actions(request)
        if not request.user.is_superuser:
            del actions['activate_backone_ab_wan_lan0']
            del actions['deactivate_backone_local_conf']

        return actions

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

    def check_ifconfig(self, request, queryset):
        for obj in queryset:
            results = run_command(obj.ipaddress, 'ifconfig')
            return render(request,
                          'admin/command_result.html',
                          context={'results': results})
    check_ifconfig.short_description = 'Check Interfaces'

    def check_firewall(self, request, queryset):
        for obj in queryset:
            results = run_command(obj.ipaddress, 'iptables -L -n')
            return render(request,
                          'admin/command_result.html',
                          context={'results': results})
    check_firewall.short_description = 'Check Firewall'

    def check_dns(self, request, queryset):
        for obj in queryset:
            results = run_command(obj.ipaddress, 'cat /etc/resolv.conf')
            return render(request,
                          'admin/command_result.html',
                          context={'results': results})
    check_dns.short_description = 'Check DNS'

    def check_routing(self, request, queryset):
        for obj in queryset:
            results = run_command(obj.ipaddress, 'netstat -nr')
            return render(request,
                          'admin/command_result.html',
                          context={'results': results})
    check_routing.short_description = 'Check Routing'

    def check_backone_status(self, request, queryset):
        for obj in queryset:
            command = 'cat /var/lib/zerotier-one/local.conf; echo;'
            command += 'backone info -j; echo;'
            command += 'backone peers; echo;'
            command += 'backone listnetworks; echo'
            results = run_command(obj.ipaddress, command)
            return render(request,
                          'admin/command_result.html',
                          context={'results': results})
    check_backone_status.short_description = 'Check BackOne Status'

    def check_backone_peers(self, request, queryset):
        for obj in queryset:
            results = run_command(obj.ipaddress, 'backone peers')
            return render(request,
                          'admin/command_result.html',
                          context={'results': results})
    check_backone_peers.short_description = 'Check BackOne Peers'

    def check_backone_networks(self, request, queryset):
        for obj in queryset:
            results = run_command(obj.ipaddress, 'backone listnetworks')
            return render(request,
                          'admin/command_result.html',
                          context={'results': results})
    check_backone_networks.short_description = 'Check BackOne Networks'

    def activate_backone_ab_wan_lan0(self, request, queryset):
        for obj in queryset:
            command = 'curl -o /tmp/config.install https://backone.cloud/installer/config.ab_wan_lan0;'
            command += 'chmod 755 /tmp/config.install;'
            command += 'cd /tmp; ./config.install'
            results = run_command(obj.ipaddress, command)
            return render(request,
                          'admin/command_result.html',
                          context={'results': results})
    activate_backone_ab_wan_lan0.short_description = 'Activate BackOne Active Backup WAN-LAN0'

    def deactivate_backone_local_conf(self, request, queryset):
        for obj in queryset:
            command = 'backone info -j;'
            command += 'rm -fr /var/lib/zerotier-one/local.conf;'
            command += '/etc/init.d/zerotier restart;'
            command += 'backone info -j'
            results = run_command(obj.ipaddress, command)
            return render(request,
                          'admin/command_result.html',
                          context={'results': results})
    deactivate_backone_local_conf.short_description = 'Deactivate BackOne local.conf'


admin.site.register(BackOne, BackOneAdmin)
