from django.contrib import admin
from .models import Contact
from django import forms
from django.core.validators import RegexValidator


class ContactAdminForm(forms.ModelForm):
    phone_regex = RegexValidator(regex=r'08([1-9])\d{7,14}',
                                 message="Nomor harus dalam format: '0899999999'. Minimal 10 dan maximal 15 digits.")
    phone = forms.CharField(
        label="Nomor HP",
        validators=[phone_regex],
        max_length=17
    )

    class Meta:
        model = Contact
        fields = '__all__'


class ContactAdmin(admin.ModelAdmin):
    form = ContactAdminForm
    list_display = ['name', 'phone']


admin.site.register(Contact, ContactAdmin)
