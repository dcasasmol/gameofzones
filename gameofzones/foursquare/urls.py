from django.conf.urls import patterns, url, include
from foursquare import views

urlpatterns = patterns('foursquare.views',
    # Receive OAuth token from 4sq.
    url(r'^callback$', views.callback, name='oauth_return'),
    # Logout from the app.
    url(r'^logout$', views.unauth, name='oauth_unauth'),
    # Authenticate with 4sq using OAuth.
    url(r'^auth$', views.auth, name='oauth_auth'),
    # Main page once logged.
    url(r'^done$', views.done, name='oauth_done'),
)
