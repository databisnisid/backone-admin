from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse
from .models import Chart, MapStatistic
from .charts import *


class ChartAdmin(admin.ModelAdmin):
    template_name = 'statistic/index.html'

    def get_urls(self):
        chart_view = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)
        return [
            path('', self.chart_view, name=chart_view),
        ]

    def chart_view(self, request):
        context_sites_per_project = sites_per_project()
        context_sites_vs_baso = sites_vs_baso()
        context_sites_per_status = sites_per_status()
        print(context_sites_per_project)
        context = {
            **self.admin_site.each_context(request),
            'total_sites': total_sites(),
            'total_projects': total_projects(),
            'total_orbits': total_orbits(),
            'total_basos': total_basos(),
            'sites_per_project': context_sites_per_project,
            'sites_vs_baso': context_sites_vs_baso,
            'sites_per_status': context_sites_per_status,
        }

        return TemplateResponse(request, self.template_name, context)


class MapStatisticAdmin(admin.ModelAdmin):
    template_name = 'statistic/map_view.html'

    def get_urls(self):
        map_view = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)
        return [
            path('', self.map_view, name=map_view),
        ]

    def map_view(self, request):
        context_sites_per_project = sites_per_project()
        context_sites_vs_baso = sites_vs_baso()
        context_sites_per_status = sites_per_status()
        context = {
            **self.admin_site.each_context(request),
            'total_sites': total_sites(),
            'total_projects': total_projects(),
            'total_orbits': total_orbits(),
            'total_basos': total_basos(),
            'sites_per_project': context_sites_per_project,
            'sites_vs_baso': context_sites_vs_baso,
            'sites_per_status': context_sites_per_status,
        }

        return TemplateResponse(request, self.template_name, context)


admin.site.register(Chart, ChartAdmin)
#admin.site.register(MapStatistic, MapStatisticAdmin)
