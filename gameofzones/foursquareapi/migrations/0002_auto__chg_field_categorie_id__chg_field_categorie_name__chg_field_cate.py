# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Categorie.id'
        db.alter_column(u'foursquareapi_categorie', 'id', self.gf('django.db.models.fields.CharField')(max_length=30, primary_key=True))

        # Changing field 'Categorie.name'
        db.alter_column(u'foursquareapi_categorie', 'name', self.gf('django.db.models.fields.CharField')(max_length=35))

        # Changing field 'Categorie.icon'
        db.alter_column(u'foursquareapi_categorie', 'icon', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'User.last_name'
        db.alter_column(u'foursquareapi_user', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'Venue.foursqueare_url'
        db.alter_column(u'foursquareapi_venue', 'foursqueare_url', self.gf('django.db.models.fields.CharField')(max_length=25))

        # Changing field 'Venue.name'
        db.alter_column(u'foursquareapi_venue', 'name', self.gf('django.db.models.fields.CharField')(max_length=40))

    def backwards(self, orm):

        # Changing field 'Categorie.id'
        db.alter_column(u'foursquareapi_categorie', 'id', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True))

        # Changing field 'Categorie.name'
        db.alter_column(u'foursquareapi_categorie', 'name', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Categorie.icon'
        db.alter_column(u'foursquareapi_categorie', 'icon', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'User.last_name'
        db.alter_column(u'foursquareapi_user', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Venue.foursqueare_url'
        db.alter_column(u'foursquareapi_venue', 'foursqueare_url', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'Venue.name'
        db.alter_column(u'foursquareapi_venue', 'name', self.gf('django.db.models.fields.CharField')(max_length=30))

    models = {
        u'foursquareapi.categorie': {
            'Meta': {'object_name': 'Categorie'},
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35'})
        },
        u'foursquareapi.checkin': {
            'Meta': {'object_name': 'Checkin'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_checkins': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'process': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['foursquareapi.User']"}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['foursquareapi.Venue']"})
        },
        u'foursquareapi.user': {
            'Meta': {'object_name': 'User'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'friends_rel_+'", 'to': u"orm['foursquareapi.User']"}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'num_friends': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'num_zones': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'photo': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'foursquareapi.venue': {
            'Meta': {'object_name': 'Venue'},
            'categorie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['foursquareapi.Categorie']"}),
            'checkins': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['foursquareapi.User']", 'through': u"orm['foursquareapi.Checkin']", 'symmetrical': 'False'}),
            'foursqueare_url': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'lon': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['foursquareapi.Zone']"})
        },
        u'foursquareapi.zone': {
            'Meta': {'object_name': 'Zone'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'king': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['foursquareapi.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'num_venues': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['foursquareapi']