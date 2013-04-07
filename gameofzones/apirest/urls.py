from apirest import views
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = patterns('apirest.views',
    # Main entry to the API.
    url(r'^$', 'api_root'),
    # Categorie list and Categorie detail for API views.
    url(r'^categories/?$', views.CategorieList.as_view(), name='categorie_list'),
    url(r'^categories/(?P<pk>[a-z0-9]+)/?$', views.CategorieDetail.as_view(), name='categorie_detail'),
    # User list and User detail for API views.
    url(r'^users/?$', views.UserList.as_view(), name='user_list'),
    url(r'^users/(?P<pk>[a-z0-9]+)/?$', views.UserDetail.as_view(), name='user_detail'),
    # Zone list and Zone detail for API views.
    url(r'^zones/?$', views.ZoneList.as_view(), name='zone_list'),
    url(r'^zones/(?P<pk>[a-z0-9]+)/?$', views.ZoneDetail.as_view(), name='zone_detail'),
    # Venue list and Venue detail for API views.
    url(r'^venues/?$', views.VenueList.as_view(), name='venue_list'),
    url(r'^venues/(?P<pk>[a-z0-9]+)/?$', views.VenueDetail.as_view(), name='venue_detail'),
    # Checkin list and Checkin detail for API views.
    url(r'^checkins/?$', views.CheckinList.as_view(), name='checkin_list'),
    url(r'^checkins/(?P<user>[a-z0-9]+)&(?P<venue>[a-z0-9]+)/?$', views.CheckinDetail.as_view(), name='checkin_detail'),
)

# Add support for format suffixes to our API endpoints.
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
