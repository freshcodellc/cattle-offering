from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('core.urls', namespace='core')),
    url(r'^account/', include('user.urls')),
    url(r'^cattle/', include('cattle.urls', namespace='cattle')),
]
