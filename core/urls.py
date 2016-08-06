from django.conf.urls import url, include
from django.views.generic import TemplateView
from .views import ContactView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
    url(r'^about', TemplateView.as_view(template_name="about.html"), name='about'),
    url(r'^offering', TemplateView.as_view(template_name="offering.html"), name='offering'),
    url(r'^thanks', TemplateView.as_view(template_name="thanks.html"), name='thanks'),
    url(r'^newsletter', TemplateView.as_view(template_name="newsletter.html"), name='newsletter'),
    url(r'^contact', ContactView.as_view(), name='contact'),
]
