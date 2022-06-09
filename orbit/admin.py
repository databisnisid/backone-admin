from django.contrib import admin
from django import forms
from .models import Orbit
from django.core.validators import RegexValidator
from .utils import get_quota_orbit


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


class OrbitAdmin(admin.ModelAdmin):
    form = OrbitAdminForm
    fields = ['username', 'password', 'msisdn', 'imei']
    readonly_fields = ['quota_total', 'quota_current', 'quota_day']
    list_display = ['imei', 'msisdn', 'quota_total', 'quota_current', 'quota_day']
    search_fields = ('msisdn', 'imei')
    actions = [check_quota]


admin.site.register(Orbit, OrbitAdmin)


