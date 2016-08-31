from django.contrib.auth.views import logout
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^register/$', views.RegistrationView.as_view(), name='register'),
    url(r'^profile/edit/(?P<pk>[-\w]+)/$', views.EditProfileView.as_view(), name='edit-profile'),
    url(r'^watchlist/$', views.WatchListView.as_view(), name='watchlist'),
    url(r'^logout/$', logout, {'next_page': '/'}),
    url('^', include('django.contrib.auth.urls')),
]
