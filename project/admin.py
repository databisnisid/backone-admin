from django.contrib import admin
from .models import Project, Po, PoVendor
from django import forms
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.admin.widgets import AdminDateWidget


class ProjectAdminForm(forms.ModelForm):
    phone_regex = RegexValidator(regex=r'08([1-9])\d{7,14}',
                                 message="Nomor harus dalam format: '08XXXXXXXX'. Minimal 10 dan maximal 15 digits.")
    name = forms.CharField(
        label='Project Name',
        widget=forms.TextInput(attrs={'placeholder': 'Nama Project contoh: PINS, CLEO, dst', 'size': 50})
    )
    contact_name = forms.CharField(
        label='Contact Name',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Nama Kontak Project', 'size': 50})
    )
    contact_email = forms.CharField(
        label='Contact Email',
        required=False,
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
    number = forms.CharField(
        label='PO Number',
        widget=forms.TextInput(attrs={'placeholder': 'Nomor PO', 'size': 50})
    )
    """
    date = forms.DateField(
        widget=forms.SelectDateWidget
    )
    """

    class Meta:
        model = Po
        fields = '__all__'


class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ['name', 'contact_name', 'contact_email', 'contact_phone']
    exclude = ['created_at', 'updated_at']

"""
class FileInNewWindowWidget(admin.widgets.AdminFileWidget):
    # AdminFileWidget inherits from django.forms.ClearableFileInput
    # The original url_markup_template in django.forms.ClearableFileInput is:
    # url_markup_template = '{1}'
    url_markup_template = '{1}'


class AttachmentInline(admin.TabularInline):
    formfield_overrides = {
       models.FileField: {'widget': FileInNewWindowWidget},
    }
"""


class PoAdmin(admin.ModelAdmin):
    #form = PoAdminForm
    #inlines = [AttachmentInline, ]
    readonly_fields = ['is_new']
    list_display = ['number', 'date', 'upload_file', 'project', 'is_new', 'is_priority']
    exclude = ['created_at', 'updated_at']

    class Meta:
        model = Po


class PoVendorAdmin(admin.ModelAdmin):
    #form = PoAdminForm
    #inlines = [AttachmentInline, ]
    list_display = ['number', 'date', 'upload_file', 'po_base', 'my_company', 'other_company']
    exclude = ['created_at', 'updated_at']

    class Meta:
        model = PoVendor


#admin.site.register(Project, ProjectAdmin)
#admin.site.register(Po, PoAdmin)
#admin.site.register(PoVendor, PoVendorAdmin)
