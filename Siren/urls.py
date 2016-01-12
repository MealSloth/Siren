from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include, url, patterns
from Siren import views

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^blog', views.blog, name='blog'),
    url(r'^about', views.about, name='about'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^consumer', views.consumer, name='consumer'),
    url(r'^producer', views.producer, name='producer'),
    url(r'^(?P<arg>[0-9A-Z]+)/$', views.detail, name='detail'),
    url(r'^test/(?P<arg>[0-9A-Z]+)/$', views.results, name='results'),
) + staticfiles_urlpatterns()
