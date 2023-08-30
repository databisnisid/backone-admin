from django.contrib import admin
from django import forms
from .models import Orbit, OrbitMulti
from django.core.validators import RegexValidator
from .utils import get_all_quota_orbit_multi, get_quota_orbit


class OrbitAdminForm(forms.ModelForm):
    phone_regex = RegexValidator(regex=r'08([1-9])\d{7,14}',
                                 message="Nomor harus dalam format: '0899999999'. Minimal 10 dan maximal 15 digits.")
    msisdn = forms.CharField(
        label='MSISDN',
        validators=[phone_regex],
        max_length=17
    )
    imei = forms.CharField(
        label='IMEI',
        widget=forms.TextInput(attrs={
                'size': 30,
            }),
    )

    class Meta:
        model = Orbit
        fields = '__all__'
        #widgets = {
        #    'username': forms.EmailInput(attrs={
        #        'size': 50,
        #    }),
        #    'password': forms.PasswordInput(attrs={
        #        'size': 50,
        #    }),
        #}


@admin.action(description='Check Quota Orbit ke myorbit.id')
def check_quota(modeladmin, request, queryset):
    for obj in queryset:
        get_quota_orbit(obj.msisdn)

@admin.action(description='Check Quota Orbit Multi ke myorbit.id')
def check_quota_multi(modeladmin, request, queryset):
    get_all_quota_orbit_multi()


class OrbitAdmin(admin.ModelAdmin):
    form = OrbitAdminForm
    #fields = ['username', 'password', 'msisdn', 'imei',
    #          'quota_total', 'quota_current', 'quota_day',]
    #          #'created_at', 'updated_at']
    fieldsets = (
        ('Orbit Login', {
            'classes': ('collapse',),
            'fields': ('username', 'password',
                       ('quota_current', 'quota_total', 'quota_day', 'updated_at'),
                       )
        }),
        ('IMEI dan MSISDN', {
            'classes': ('collapse',),
            'fields': ('imei', 'msisdn',)
        }),
        ('Site dan Keterangan', {
            'classes': ('collapse',),
            'fields': ('site', 'additional_info',)
        }),
    )
    readonly_fields = ['quota_total', 'quota_current', 'quota_day',
                       'created_at', 'updated_at']
    list_display = ['imei', 'msisdn', 'site', 'quota_total', 'quota_current', 'quota_day', 'updated_at', 'additional_info']
    search_fields = ('msisdn', 'imei', 'additional_info')
    actions = [check_quota]


class OrbitMultiAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Orbit Login', {
            'classes': ('collapse',),
            'fields': ('username', 'password',
                       ('quota_current', 'quota_total', 'quota_day', 'updated_at'),
                       )
        }),
        ('IMEI dan MSISDN', {
            'classes': ('collapse',),
            'fields': ('imei', 'msisdn',)
        }),
        ('Site dan Keterangan', {
            'classes': ('collapse',),
            'fields': ('site', 'additional_info',)
        }),
    )
    readonly_fields = ['msisdn', 'quota_total', 'quota_current', 'quota_day',
                       'created_at', 'updated_at']
    list_display = ['msisdn', 'site', 'quota_total', 'quota_current', 'quota_day', 'updated_at', 'additional_info']
    search_fields = ('msisdn', 'additional_info')
    actions = [check_quota_multi]


admin.site.register(Orbit, OrbitAdmin)
admin.site.register(OrbitMulti, OrbitMultiAdmin)


