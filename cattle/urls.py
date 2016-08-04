from django.conf.urls import url, include
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
    url(r'^about', TemplateView.as_view(template_name="about.html"), name='index'),
    url(r'^offering', TemplateView.as_view(template_name="offering.html"), name='index'),
    url(r'^newsletter', TemplateView.as_view(template_name="newsletter.html"), name='index'),
    url(r'^contact', TemplateView.as_view(template_name="contact.html"), name='index'),
]
