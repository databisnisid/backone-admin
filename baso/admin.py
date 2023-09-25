from django.contrib import admin
from django import forms
from .models import Baso


class BasoAdminForm(forms.ModelForm):
    name = forms.CharField(
        label='Nomor',
        widget=forms.TextInput(attrs={
            'size': 20
        })
    )

    class Meta:
        model = Baso
        fields = '__all__'


class BasoAdmin(admin.ModelAdmin):
    form = BasoAdminForm
    list_display = ['name', 'date', 'upload_file']
    exclude = ['created_at', 'updated_at']

    class Meta:
        model = Baso


#admin.site.register(Baso, BasoAdmin)
