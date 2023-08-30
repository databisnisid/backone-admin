"""
from django.contrib import admin
from .views import index
from .models import Map
from django.urls import path
from backone.models import BackOne
from django.conf import settings
from django.template.response import TemplateResponse


class MapAdmin(admin.ModelAdmin):
    template_name = 'map_admin.html'

    def get_urls(self):
        map_view = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name
        )
        my_urls = [
            path('', self.map_view, name=map_view)
        ]
        return my_urls

    def map_view(self, request):
        backone = BackOne.objects.all()
        return TemplateResponse(request, self.template_name, {'backone': backone, 'settings': settings})


admin.site.register(Map, MapAdmin)
"""
