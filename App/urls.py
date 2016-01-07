from django.conf.urls import url
from App import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<arg>[0-9A-Z]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^test/(?P<arg>[0-9A-Z]+)/$', views.results, name='results'),
]