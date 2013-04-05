# Create yours views here.

import json
from urllib import urlencode
from urllib2 import urlopen, Request

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.serializers import serialize
from django.contrib.auth import logout

from foursquare.models import Categorie, User, Zone, Venue, Checkin
from foursquare.utils import get_datetime, get_timestamp_month_ago
from foursquare.utils import process_user, process_checkins
from foursquare.utils import get_data_database

# Settings for foursquare login.
CLIENT_ID = 'ZGS2B13AJH3RN03KB1O4YWEGRXAXUUZK2WVPYTA0WBZA1R22'
CLIENT_SECRET = 'ISCNHPBWZWMOHXFN22Y1GVA3DX31QYUIFSWPHKQEV5I3ASHK'

request_token_url = 'https://es.foursquare.com/oauth2/authenticate'
access_token_url = 'https://es.foursquare.com/oauth2/access_token'
redirect_url = 'http://localhost:8000/foursquare/callback'


def auth(request):
    # Build the url to request.
    params = {'client_id': CLIENT_ID,
            'response_type': 'code',
            'redirect_uri': redirect_url}
    data = urlencode(params)
    # Redirect the user to the url to confirm access for the app.
    return HttpResponseRedirect('%s?%s' % (request_token_url, data))


def unauth(request):
    # Clear any tokens and logout.
    request.session.clear()
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def callback(request):
    # Get the code returned from foursquare.
    code = request.GET.get('code')

    # Build the url to request the access_token.
    params = {'client_id': CLIENT_ID,
           'client_secret': CLIENT_SECRET,
           'grant_type': 'authorization_code',
           'redirect_uri': redirect_url,
           'code': code}
    data = urlencode(params)
    req = Request(access_token_url, data)

    # Request the access_token.
    response = urlopen(req)
    access_token = json.loads(response.read())
    access_token = access_token['access_token']

    # Store the access_token for later use.
    request.session['access_token'] = access_token

    # Redirect the user to show we're done.
    return HttpResponseRedirect(reverse('oauth_done'))


def done(request):
    # Get the access_token.
    access_token = request.session.get('access_token')

    # Request user details from foursquare.
    api = 'https://api.foursquare.com/v2/'
    endpoint = 'users/self'
    params = {'oauth_token': access_token,
              'v': get_datetime(),
    }
    # Build the url to user's request.
    url = '%s%s?%s' % (api, endpoint, urlencode(params))
    user = urlopen(url)
    user = user.read()
    user = json.loads(user)['response']['user']
    user = process_user(user)

    # Optional user details from foursquare.
    extra_params = {'afterTimestamp': get_timestamp_month_ago(),
              'limit': 250,
    }
    # Build the url to checkins's request.
    endpoint = 'users/self/checkins'
    url = '%s%s?%s&%s' % (api, endpoint, urlencode(extra_params),
                         urlencode(params))
    checkins = urlopen(url)
    checkins = checkins.read()
    checkins = json.loads(checkins)['response']['checkins']['items']
    process_checkins(user, checkins)

    database = serialize('json', Zone.objects.all())

    # Show the page with the user's name to show they've logged in.
    return render_to_response('done.html', {'database': database},
                              context_instance=RequestContext(request))
