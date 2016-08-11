from django.conf.urls import url, include
from django.views.generic import TemplateView
from .views import CattleListView

urlpatterns = [
    url(r'^offering', CattleListView.as_view(), name='offering'),
]
