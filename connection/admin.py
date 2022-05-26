from django.contrib import admin
from .models import ConnectionType


class ConnectionTypeAdmin(admin.ModelAdmin):
    fields = ['name']

admin.site.register(ConnectionType, ConnectionTypeAdmin)