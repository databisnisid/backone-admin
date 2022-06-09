from django.contrib import admin
from django.urls import path
from .views import get_quota_current, get_quota_day, SiteReport

urlpatterns = [
    path('report/', SiteReport.as_view(), name='sitereport'),
    path('q_current/<ipaddress>', get_quota_current, name='get_quota_current'),
    path('q_day/<ipaddress>', get_quota_day, name='get_quota_day'),
]