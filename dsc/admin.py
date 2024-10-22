from django.contrib import admin
from django import forms
from .models import DscDpi, DscDpiProit
from django.core.validators import RegexValidator

# from .utils import get_all_quota_orbit_multi, get_quota_orbit


class DscDpiAdminForm(forms.ModelForm):
    phone_regex = RegexValidator(
        regex=r"628([1-9])\d{7,14}",
        message="Nomor harus dalam format: '62899999999'. Minimal 10 dan maximal 16 digits.",
    )
    msisdn = forms.CharField(label="MSISDN", validators=[phone_regex], max_length=17)

    class Meta:
        model = DscDpi
        fields = "__all__"


class DscDpiProitAdminForm(forms.ModelForm):
    phone_regex = RegexValidator(
        regex=r"628([1-9])\d{7,14}",
        message="Nomor harus dalam format: '62899999999'. Minimal 10 dan maximal 16 digits.",
    )
    msisdn = forms.CharField(label="MSISDN", validators=[phone_regex], max_length=17)

    class Meta:
        model = DscDpiProit
        fields = "__all__"


"""
@admin.action(description='Check Quota Orbit ke myorbit.id')
def check_quota(modeladmin, request, queryset):
    for obj in queryset:
        get_quota_orbit(obj.msisdn)

@admin.action(description='Check Quota Orbit Multi ke myorbit.id')
def check_quota_multi(modeladmin, request, queryset):
    get_all_quota_orbit_multi()
"""


class DscDpiAdmin(admin.ModelAdmin):
    form = DscDpiAdminForm
    # fields = ['username', 'password', 'msisdn', 'imei',
    #          'quota_total', 'quota_current', 'quota_day',]
    #          #'created_at', 'updated_at']
    fieldsets = (
        (
            "MSISDN",
            {
                "classes": ("collapse",),
                "fields": (
                    "msisdn",
                    ("quota_current", "quota_day", "quota_date", "updated_at"),
                ),
            },
        ),
        (
            "Site dan Keterangan",
            {
                "classes": ("collapse",),
                "fields": ("site", "additional_info", "error_msg"),
            },
        ),
    )
    readonly_fields = [
        "quota_current",
        "quota_until",
        "quota_date",
        "quota_day",
        "created_at",
        "updated_at",
    ]
    list_display = [
        "msisdn",
        "site",
        "quota_current",
        "quota_day",
        "updated_at",
        "additional_info",
        "error_msg",
    ]
    search_fields = ("msisdn", "additional_info")
    # actions = [check_quota]


class DscDpiProitAdmin(admin.ModelAdmin):
    form = DscDpiProitAdminForm
    # fields = ['username', 'password', 'msisdn', 'imei',
    #          'quota_total', 'quota_current', 'quota_day',]
    #          #'created_at', 'updated_at']
    fieldsets = (
        (
            "MSISDN",
            {
                "classes": ("collapse",),
                "fields": (
                    "msisdn",
                    ("quota_current", "quota_day", "quota_date", "updated_at"),
                ),
            },
        ),
        (
            "Site dan Keterangan",
            {
                "classes": ("collapse",),
                "fields": ("site", "additional_info", "error_msg"),
            },
        ),
    )
    readonly_fields = [
        "quota_current",
        "quota_until",
        "quota_date",
        "quota_day",
        "created_at",
        "updated_at",
    ]
    list_display = [
        "msisdn",
        "site",
        "quota_current",
        "quota_day",
        "updated_at",
        "additional_info",
        "error_msg",
    ]
    search_fields = ("msisdn", "additional_info")
    # actions = [check_quota]


admin.site.register(DscDpi, DscDpiAdmin)
admin.site.register(DscDpiProit, DscDpiProitAdmin)
