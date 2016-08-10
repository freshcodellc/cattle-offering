from django.contrib.auth.views import logout
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^signup/$', views.Signup.as_view(), name='signup'),
    url(r'^logout/$', logout, {'next_page': '/'}),
    url('^', include('django.contrib.auth.urls')),
]
