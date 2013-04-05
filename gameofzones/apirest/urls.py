from apirest import views
from django.conf.urls import patterns, url

urlpatterns = patterns('apirest.views',
    url(r'^categories/$', 'CategorieList'),
    url(r'^categories/(?P<id>[a-z0-9]+)/$', 'CategorieDetail'),

    url(r'^users/$', 'UserList'),
    url(r'^users/(?P<id>[a-z0-9]+)/$', 'UserDetail'),

    url(r'^zones/$', 'ZoneList'),
    url(r'^zones/(?P<id>[a-z0-9]+)/$', 'ZoneDetail'),

    url(r'^venues/$', 'VenueList'),
    url(r'^venues/(?P<id>[a-z0-9]+)/$', 'VenueDetail'),

    url(r'^checkins/$', 'CheckinList'),
    url(r'^checkins/(?P<user>[a-z0-9]+)&(?P<venue>[a-z0-9]+)/$', 'CheckinDetail'),
)
