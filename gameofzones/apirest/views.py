# Create your views here.

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from foursquare.models import Categorie, User, Zone, Venue, Checkin
from foursquare.serializers import CategorieSerializer, UserSerializer, ZoneSerializer, VenueSerializer, CheckinSerializer

# Subclass of HttpResponse that render any data returned into json.
class JSONResponse(HttpResponse):
    # An HttpResponse that renders it's content into JSON.
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)



# View which lists all the existing categories, or creating a new categorie.
@csrf_exempt
def CategorieList(request):
    # List all categories, or create a new categorie.
    if request.method == 'GET':
        categories = Categorie.objects.all()
        serializer = CategorieSerializer(categories, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategorieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
            return JSONResponse(serializer.errors, status=400)


# View which corresponds to an individual categorie, and can be used to retrieve, update or delete the categorie.
@csrf_exempt
def CategorieDetail(request, id):
    # Retrieve, update or delete a categorie.
    try:
        categorie = Categorie.objects.get(id=id)
    except Categorie.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CategorieSerializer(categorie)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CategorieSerializer(categorie, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        else:
            return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        categorie.delete()
        return HttpResponse(status=204)



# View which lists all the existing users, or creating a new user.
@csrf_exempt
def UserList(request):
    # List all users, or create a new user.
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
            return JSONResponse(serializer.errors, status=400)


# View which corresponds to an individual user, and can be used to retrieve, update or delete the user.
@csrf_exempt
def UserDetail(request, id):
    # Retrieve, update or delete a user.
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        else:
            return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)



# View which lists all the existing zones, or creating a new zone.
@csrf_exempt
def ZoneList(request):
    # List all zones, or create a new zone.
    if request.method == 'GET':
        zones = Zone.objects.all()
        serializer = ZoneSerializer(zones, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ZoneSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
            return JSONResponse(serializer.errors, status=400)


# View which corresponds to an individual zone, and can be used to retrieve, update or delete the zone.
@csrf_exempt
def ZoneDetail(request, id):
    # Retrieve, update or delete a zone.
    try:
        zone = Zone.objects.get(id=id)
    except Zone.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ZoneSerializer(zone)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ZoneSerializer(zone, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        else:
            return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        zone.delete()
        return HttpResponse(status=204)



# View which lists all the existing venues, or creating a new venue.
@csrf_exempt
def VenueList(request):
    # List all venues, or create a new venue.
    if request.method == 'GET':
        venues = Venue.objects.all()
        serializer = VenueSerializer(venues, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VenueSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
            return JSONResponse(serializer.errors, status=400)


# View which corresponds to an individual venue, and can be used to retrieve, update or delete the venue.
@csrf_exempt
def VenueDetail(request, id):
    # Retrieve, update or delete a venue.
    try:
        venue = Venue.objects.get(id=id)
    except Venue.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = VenueSerializer(venue)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VenueSerializer(venue, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        else:
            return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        venue.delete()
        return HttpResponse(status=204)



# View which lists all the existing checkins, or creating a new checkin.
@csrf_exempt
def CheckinList(request):
    # List all checkins, or create a new checkin.
    if request.method == 'GET':
        checkins = Checkin.objects.all()
        serializer = CheckinSerializer(checkins, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CheckinSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
            return JSONResponse(serializer.errors, status=400)


# View which corresponds to an individual checkin, and can be used to retrieve, update or delete the checkin.
@csrf_exempt
def CheckinDetail(request, user, venue):
    # Retrieve, update or delete a checkin.
    try:
        checkin = Checkin.objects.get(user=user, venue=venue)
    except Checkin.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CheckinSerializer(checkin)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CheckinSerializer(checkin, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        else:
            return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        checkin.delete()
        return HttpResponse(status=204)
