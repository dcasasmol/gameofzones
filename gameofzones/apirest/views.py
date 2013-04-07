# Create your views here.

from django.http import Http404
from rest_framework import status, generics, permissions, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from foursquare.models import Categorie, User, Zone, Venue, Checkin
from foursquare.serializers import CategorieSerializer, UserSerializer, ZoneSerializer, VenueSerializer, CheckinSerializer


# Single entry point to the API
@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'categories': reverse('categorie_list', request=request, format=format),
        'users': reverse('user_list', request=request, format=format),
        'zones': reverse('zone_list', request=request, format=format),
        'venues': reverse('venue_list', request=request, format=format),
        'checkins': reverse('checkin_list', request=request, format=format)
    })



# Class which lists all the existing categories, or creates a new categorie.
class CategorieList(generics.ListCreateAPIView):
    model = Categorie
    serializer_class = CategorieSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# Class which corresponds to an individual categorie, and can be used to retrieve, update or delete the categorie.
class CategorieDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Categorie
    serializer_class = CategorieSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



# Class which lists all the existing users, or creates a new user.
class UserList(generics.ListCreateAPIView):
    model = User
    serializer_class = UserSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# Class which corresponds to an individual user, and can be used to retrieve, update or delete the user.
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = UserSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



# Class which lists all the existing zones, or creates a new zone.
class ZoneList(generics.ListCreateAPIView):
    model = Zone
    serializer_class = ZoneSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# Class which corresponds to an individual zone, and can be used to retrieve, update or delete the zone.
class ZoneDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Zone
    serializer_class = ZoneSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



# Class which lists all the existing venues, or creates a new venue.
class VenueList(generics.ListCreateAPIView):
    model = Venue
    serializer_class = VenueSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# Class which corresponds to an individual venue, and can be used to retrieve, update or delete the venue.
class VenueDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Venue
    serializer_class = VenueSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



# Class which lists all the existing checkins, or creates a new checkin.
class CheckinList(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    # List all checkins.
    def get(self, request, format=None):
        checkins = Checkin.objects.all()
        serializer = CheckinSerializer(checkins, many=True)
        return Response(serializer.data)
    # Create a new checkin.
    def post(self, request, format=None):
        serializer = CheckinSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Class which corresponds to an individual checkin, and can be used to retrieve, update or delete the checkin.
class CheckinDetail(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    # Check if a checkin instance exists.
    def get_object(self, user, venue):
        try:
            return Checkin.objects.get(user=user, venue=venue)
        except Checkin.DoesNotExist:
            raise Http404
    # Retrieve a checkin instance.
    def get(self, request, user, venue, format=None):
        checkin = self.get_object(user, venue)
        serializer = CheckinSerializer(checkin)
        return Response(serializer.data)
    # Update a checkin instance.
    def put(self, request, user, venue, format=None):
        checkin = self.get_object(user, venue)
        serializer = CheckinSerializer(checkin, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Delete a checkin instance.
    def delete(self, request, user, venue, format=None):
        checkin = self.get_object(user, venue)
        checkin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
