from django.contrib import admin
from .models import Project, Po
from django import forms
from django.core.validators import RegexValidator


class ProjectAdminForm(forms.ModelForm):
    phone_regex = RegexValidator(regex=r'08([1-9])\d{7,14}',
                                 message="Nomor harus dalam format: '08XXXXXXXX'. Minimal 10 dan maximal 15 digits.")
    name = forms.CharField(
        label='Project Name',
        widget=forms.TextInput(attrs={'placeholder': 'Nama Project contoh: PINS, CLEO, dst', 'size': 50})
    )
    contact_name = forms.CharField(
        label='Contact Name',
        widget=forms.TextInput(attrs={'placeholder': 'Nama Kontak Project', 'size': 50})
    )
    contact_email = forms.CharField(
        label='Contact Email',
        widget=forms.TextInput(attrs={'placeholder': 'Email Kontak Project', 'size': 50})
    )

    contact_phone = forms.CharField(
        label='Contact HP',
        validators=[phone_regex],
        max_length=17,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '08XXXXXXXX', 'size': 20})
    )

    class Meta:
        model = Project
        fields = '__all__'


class PoAdminForm(forms.ModelForm):
    po_number = forms.CharField(
        label='PO Number',
        widget=forms.TextInput(attrs={'placeholder': 'Nomor PO', 'size': 50})
    )

    class Meta:
        model = Po
        fields = '__all__'


class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ['name', 'contact_name', 'contact_email', 'contact_phone']
    exclude = ['created_at', 'updated_at']


class PoAdmin(admin.ModelAdmin):
    form = PoAdminForm
    list_display = ['po_number', 'po_date', 'project']

    class Meta:
        model = Po


admin.site.register(Project, ProjectAdmin)
admin.site.register(Po, PoAdmin)
