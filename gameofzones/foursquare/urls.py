from django.conf.urls.defaults import patterns, url, include
from foursquare import views

urlpatterns = patterns('foursquare.views',
    # receive OAuth token from 4sq
    url(r'^callback$', views.callback, name='oauth_return'),
    # logout from the app
    url(r'^logout$', views.unauth, name='oauth_unauth'),
    # authenticate with 4sq using OAuth
    url(r'^auth$', views.auth, name='oauth_auth'),
    # main page once logged
    url(r'^done$', views.done, name='oauth_done'),
)
