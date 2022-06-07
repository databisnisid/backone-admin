from django.contrib import admin
from .models import MyCompany, OtherCompany


class MyCompanyAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        model = MyCompany


class OtherCompanyAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        model = OtherCompany


admin.site.register(MyCompany, MyCompanyAdmin)
admin.site.register(OtherCompany, OtherCompanyAdmin)
