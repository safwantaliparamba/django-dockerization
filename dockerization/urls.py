from django.urls import path, include

from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings as SETTINGS


urlpatterns = [
    path("", include("web.urls")),
    path('admin/', admin.site.urls),
]

urlpatterns += static(SETTINGS.STATIC_URL, document_root=SETTINGS.STATIC_ROOT)
urlpatterns += static(SETTINGS.MEDIA_URL, document_root=SETTINGS.MEDIA_ROOT)
