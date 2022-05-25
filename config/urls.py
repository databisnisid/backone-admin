from django.contrib import admin
from django.urls import path, include
from landing.views import index


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('backone/', include('backone.urls')),
    path('landing/', include('landing.urls')),
]
