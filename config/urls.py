from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from landing.views import index
from orbit.views import get_quota_all_orbit, get_quota_all_orbit_multi, get_quota


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('sites/', include('backone.urls')),
    path('landing/', include('landing.urls')),
    path('quota/all_orbit/', get_quota_all_orbit, name='all_orbit'),
    path('quota/all_orbit_multi/', get_quota_all_orbit_multi, name='all_orbit_multi'),
    path('quota/<str:msisdn>/', get_quota, name='get_quota'),
    #path('statistic/', include('statistic.urls')),
]

if not settings.PRODUCTION:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
