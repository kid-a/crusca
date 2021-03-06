from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from clouds.models import Cloud

admin.autodiscover()
admin.site.register(Cloud)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pywordcloud.views.home', name='home'),
    # url(r'^pywordcloud/', include('pywordcloud.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
