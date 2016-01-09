from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include, url, patterns
from Siren import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^(?P<arg>[0-9A-Z]+)/$', views.detail, name='detail'),
    url(r'^test/(?P<arg>[0-9A-Z]+)/$', views.results, name='results'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
) + staticfiles_urlpatterns()
