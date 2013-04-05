# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Checkin', fields ['venue', 'user']
        db.create_unique(u'foursquare_checkin', ['venue_id', 'user_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Checkin', fields ['venue', 'user']
        db.delete_unique(u'foursquare_checkin', ['venue_id', 'user_id'])


    models = {
        u'foursquare.categorie': {
            'Meta': {'object_name': 'Categorie'},
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35'})
        },
        u'foursquare.checkin': {
            'Meta': {'ordering': "['user', '-num_checkins']", 'unique_together': "(('user', 'venue'),)", 'object_name': 'Checkin'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_checkins': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'process': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['foursquare.User']"}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['foursquare.Venue']"})
        },
        u'foursquare.user': {
            'Meta': {'object_name': 'User'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'friends_rel_+'", 'blank': 'True', 'to': u"orm['foursquare.User']"}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'num_friends': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'num_zones': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'photo': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'foursquare.venue': {
            'Meta': {'object_name': 'Venue'},
            'categorie': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'venues'", 'to': u"orm['foursquare.Categorie']"}),
            'checkins': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['foursquare.User']", 'through': u"orm['foursquare.Checkin']", 'symmetrical': 'False'}),
            'foursquare_url': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'lon': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'venues'", 'to': u"orm['foursquare.Zone']"})
        },
        u'foursquare.zone': {
            'Meta': {'object_name': 'Zone'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'king': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'kingdoms'", 'to': u"orm['foursquare.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'num_venues': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['foursquare']