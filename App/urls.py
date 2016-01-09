from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url, patterns
from App import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<arg>[0-9A-Z]+)/$', views.detail, name='detail'),
    url(r'^test/(?P<arg>[0-9A-Z]+)/$', views.results, name='results'),
) + staticfiles_urlpatterns()
