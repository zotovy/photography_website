from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from website.views import home_view, preset_view
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),

    path('preset/<slug:slug>/', preset_view, name='preset'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
