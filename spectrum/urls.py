from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'spectrum.views.home', name='home'),
    # url(r'^spectrum/', include('spectrum.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^gallery/', include('gallery.urls', namespace="gallery")),
    url(r'^admin/', include(admin.site.urls)),
)
