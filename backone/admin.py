from django.contrib import admin
from .models import BackOne
from django import forms


class BackOneAdminForm(forms.ModelForm):
    class Meta:
        model = BackOne
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput
        }


class BackOneAdmin(admin.ModelAdmin):
    form = BackOneAdminForm
    fields = ['name', 'ipaddress',
              'location', 'backone_network', 'description', 'orbit',
              'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    list_display = ['name', 'ipaddress', 'location', 'orbit']
    list_filter = ('name', 'ipaddress',)


admin.site.register(BackOne, BackOneAdmin)

