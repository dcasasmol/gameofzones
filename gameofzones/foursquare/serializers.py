from rest_framework import serializers
from foursquare.models import Categorie, User, Zone, Venue, Checkin


# Class to serializing the Categorie instances into representations such as json.
class CategorieSerializer(serializers.ModelSerializer):
    venues = serializers.RelatedField(many=True)

    class Meta:
        model = Categorie
        fields = ('id', 'name', 'icon', 'venues')


# Class to serializing the Categorie instances into reduced representations such as json.
class CategorieSerializerReduced(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ('id', 'name', 'icon')


# Class to serializing the User instances into representations such as json.
class UserSerializer(serializers.ModelSerializer):
    kingdoms = serializers.RelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'gender', 'photo', 'city', 'bio', 'email', 'facebook', 'twitter', 'points', 'kingdoms', 'num_zones', 'friends', 'num_friends')


# Class to serializing the User instances into reduced representations such as json.
class UserSerializerReduced(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'gender', 'photo', 'city')


# Class to serializing the Venue instances into representations such as json.
class VenueSerializer(serializers.ModelSerializer):
    categorie = CategorieSerializerReduced()
    zone = serializers.Field(source = 'zone.id')

    class Meta:
        model = Venue
        fields = ('id', 'name', 'lat', 'lon', 'foursquare_url', 'categorie', 'zone', 'checkins')


# Class to serializing the Zone instances into representations such as json.
class ZoneSerializer(serializers.ModelSerializer):
    king = UserSerializerReduced()
    venues = VenueSerializer(many=True)

    class Meta:
        model = Zone
        fields = ('id', 'name', 'king', 'venues', 'num_venues')


# Class to serializing the Checkin instances into representations such as json.
class CheckinSerializer(serializers.ModelSerializer):
    user = UserSerializerReduced()
    venue = VenueSerializer()

    class Meta:
        model = Checkin
        fields = ('user', 'venue', 'num_checkins')
