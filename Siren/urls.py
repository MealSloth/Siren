from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include, url, patterns
from Siren import views

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^(?P<arg>[0-9A-Z]+)/$', views.detail, name='detail'),
    url(r'^test/(?P<arg>[0-9A-Z]+)/$', views.results, name='results'),
) + staticfiles_urlpatterns()
