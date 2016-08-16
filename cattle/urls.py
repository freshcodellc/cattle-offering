from django.conf.urls import url
from django.views.generic import TemplateView

from .views import CattleDetailView, CattleListView, ImportCattleView

urlpatterns = [
    url(r'^offering/(?P<pk>[-\w]+)/$', CattleDetailView.as_view(), name='offering-detail'),
    url(r'^offering', CattleListView.as_view(), name='offering'),
    url(r'^import', ImportCattleView.as_view(), name='import-cattle'),
    url(r'^success', TemplateView.as_view(template_name='cattle/success.html'), name='success')
]
