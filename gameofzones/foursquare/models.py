# Create your models here.
from django.db import models


# Categorie class.
class Categorie(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=35)
    icon = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

# User class.
class User(models.Model):
    GENDER_CHOICES = (
        (u'male', u'male'),
        (u'female', u'female'),
    )

    id = models.CharField(max_length=30, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True)
    photo = models.CharField(max_length=30)
    city = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    facebook = models.CharField(max_length=20, blank=True)
    twitter = models.CharField(max_length=20, blank=True)
    points = models.IntegerField(default=0)
    num_zones = models.IntegerField(default=0)
    friends = models.ManyToManyField('self', blank=True)
    num_friends = models.IntegerField(default=0)

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)


# Zone class.
class Zone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    king = models.ForeignKey(User, related_name='kingdoms')
    num_venues = models.IntegerField(default=0)

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return self.name


# Venue class.
class Venue(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=80)
    lat = models.CharField(max_length=25)
    lon = models.CharField(max_length=25)
    foursquare_url = models.CharField(max_length=25)
    categorie = models.ForeignKey(Categorie, related_name='venues')
    zone = models.ForeignKey(Zone, related_name='venues')
    checkins = models.ManyToManyField(User, through='Checkin')

    def __unicode__(self):
        return self.name


# Checkin class.
class Checkin(models.Model):
    user = models.ForeignKey(User)
    venue = models.ForeignKey(Venue)
    num_checkins = models.IntegerField(default=0)
    process = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user', 'venue')
        ordering = ['user', '-num_checkins']

    def __unicode__(self):
        if self.num_checkins == 1:
            return u'%s en %s, %s vez' % (self.user, self.venue, self.num_checkins)
        else:
            return u'%s en %s, %s veces' % (self.user, self.venue, self.num_checkins)

