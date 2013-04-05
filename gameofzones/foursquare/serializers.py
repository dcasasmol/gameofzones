from rest_framework import serializers
from foursquare.models import Categorie, User, Zone, Venue, Checkin

class CategorieSerializer(serializers.ModelSerializer):
    venues = serializers.RelatedField(many=True)

    class Meta:
        model = Categorie
        fields = ('id', 'name', 'icon', 'venues')


class UserSerializer(serializers.ModelSerializer):
    kingdoms = serializers.RelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'gender', 'photo', 'city', 'bio', 'email', 'facebook', 'twitter', 'points', 'kingdoms', 'num_zones', 'friends', 'num_friends')


class ZoneSerializer(serializers.ModelSerializer):
    venues = serializers.RelatedField(many=True)

    class Meta:
        model = Zone
        fields = ('id', 'name', 'king', 'venues', 'num_venues')


class VenueSerializer(serializers.ModelSerializer):
    categorie = serializers.Field(source = 'categorie.name')
    zone = serializers.Field(source = 'zone.name')

    class Meta:
        model = Venue
        fields = ('id', 'name', 'lat', 'lon', 'foursquare_url', 'categorie', 'zone', 'checkins')


class CheckinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkin
        fields = ('user', 'venue', 'num_checkins')
