from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('core.urls', namespace='core')),
    url(r'^account/', include('user.urls')),
    url(r'^cattle/', include('cattle.urls', namespace='cattle')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
