# Create your models here.
from django.db import models


# Categorie class.
class Categorie(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=35)
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# User class.
class User(models.Model):
    GENDER_CHOICES = (
        (u'male', u'male'),
        (u'female', u'female'),
    )

    id = models.CharField(max_length=20, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True)
    photo = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    facebook = models.CharField(max_length=20, blank=True)
    twitter = models.CharField(max_length=20, blank=True)
    points = models.IntegerField(default=0)
    num_zones = models.IntegerField(default=0)
    friends = models.ManyToManyField('self')
    num_friends = models.IntegerField(default=0)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


# Zone class.
class Zone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    king = models.ForeignKey(User)
    num_venues = models.IntegerField(default=0)

    def __str__(self):
        return self.name


# Venue class.
class Venue(models.Model):
    id = models.CharField(max_length=25, primary_key=True)
    name = models.CharField(max_length=40)
    lat = models.CharField(max_length=25)
    lon = models.CharField(max_length=25)
    foursqueare_url = models.CharField(max_length=25)
    categorie = models.ForeignKey(Categorie)
    zone = models.ForeignKey(Zone)
    checkins = models.ManyToManyField(User, through='Checkin')

    def __str__(self):
        return self.name


# Checkin class.
class Checkin(models.Model):
    user = models.ForeignKey(User)
    venue = models.ForeignKey(Venue)
    num_checkins = models.IntegerField(default=0)
    process = models.BooleanField(default=True)

    def __str__(self):
        return '%s en %s, %s veces' % (self.user, self.venue, self.num_checkins)
