from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^signup/$', views.Signup.as_view(), name='signup'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url('^', include('django.contrib.auth.urls')),
]
