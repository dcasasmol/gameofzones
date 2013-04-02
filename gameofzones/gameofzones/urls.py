from django.conf.urls import patterns, include, url
from gameofzones import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),
    # url(r'^gameofzones/', include('gameofzones.foo.urls')),
    url(r'^foursquare/', include('foursquare.urls')),
    url(r'^maintenance/', views.maintenance,
        name='maintenance'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
