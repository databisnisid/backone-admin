from django.contrib import admin
from .models import ConnectionType, ConnectionStatus


class ConnectionTypeAdmin(admin.ModelAdmin):
    fields = ['name']


class ConnectionStatusAdmin(admin.ModelAdmin):
    fields = ['name']


admin.site.register(ConnectionType, ConnectionTypeAdmin)
admin.site.register(ConnectionStatus, ConnectionStatusAdmin)
