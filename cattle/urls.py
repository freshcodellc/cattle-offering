from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^offering/(?P<pk>[-\w]+)/$', views.CattleDetailView.as_view(), name='offering-detail'),
    url(r'^offering/(?P<pk>[-\w]+)/(?P<action>[\w\-]+)/$', views.ToggleCattleWatchView.as_view(), name='offering-toggle-watch'),
    url(r'^offering', views.CattleFilterListView.as_view(), name='offering'),
    url(r'^import', views.ImportCattleView.as_view(), name='import-cattle'),
    url(r'^success', TemplateView.as_view(template_name='cattle/success.html'), name='success')
]
