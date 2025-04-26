from django.contrib import admin
from django import forms
from .models import Starlink


class StarlinkAdminForm(forms.ModelForm):

    class Meta:
        model = Starlink
        fields = "__all__"


class StarlinkAdmin(admin.ModelAdmin):
    # form = DscDpiAdminForm
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
                    "kit_serialnumber",
                    "activation_date",
                    (
                        "quota_usage",
                        "quota_current",
                        "quota_day",
                        "quota_date",
                        "updated_at",
                    ),
                ),
            },
        ),
        (
            "Site dan Keterangan",
            {"classes": ("collapse",), "fields": ("site", "additional_info")},
        ),
    )
    readonly_fields = [
        "quota_current",
        "quota_until",
        "quota_date",
        "quota_day",
        "quota_usage",
        "created_at",
        "updated_at",
    ]
    list_display = [
        "msisdn",
        "kit_serialnumber",
        "site",
        "quota_usage",
        "quota_current",
        "quota_day",
        "activation_date",
        "updated_at",
        "additional_info",
    ]
    search_fields = ("msisdn", "additional_info")
    # actions = [check_quota]


admin.site.register(Starlink, StarlinkAdmin)
