from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^', include('user.urls', namespace='user')),
    # url(r'^', include('cattle.urls', namespace='cattle')),
]
