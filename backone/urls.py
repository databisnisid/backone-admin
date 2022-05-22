from django.contrib import admin
from django.urls import path
from .views import get_quota_current, get_quota_day

urlpatterns = [
    path('q_current/<ipaddress>', get_quota_current, name='get_quota_current'),
    path('q_day/<ipaddress>', get_quota_day, name='get_quota_day'),
]