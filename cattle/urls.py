from django.conf.urls import url, include
from django.views.generic import TemplateView
from .views import CattleListView, CattleDetailView

urlpatterns = [
    url(r'^offering/(?P<pk>[-\w]+)/$', CattleDetailView.as_view(), name='offering-detail'),
    url(r'^offering', CattleListView.as_view(), name='offering'),
]
