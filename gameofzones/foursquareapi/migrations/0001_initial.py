# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Categorie'
        db.create_table(u'foursquareapi_categorie', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('icon', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'foursquareapi', ['Categorie'])

        # Adding model 'User'
        db.create_table(u'foursquareapi_user', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('photo', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('facebook', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('points', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('num_zones', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('num_friends', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'foursquareapi', ['User'])

        # Adding M2M table for field friends on 'User'
        db.create_table(u'foursquareapi_user_friends', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_user', models.ForeignKey(orm[u'foursquareapi.user'], null=False)),
            ('to_user', models.ForeignKey(orm[u'foursquareapi.user'], null=False))
        ))
        db.create_unique(u'foursquareapi_user_friends', ['from_user_id', 'to_user_id'])

        # Adding model 'Zone'
        db.create_table(u'foursquareapi_zone', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('king', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foursquareapi.User'])),
            ('num_venues', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'foursquareapi', ['Zone'])

        # Adding model 'Venue'
        db.create_table(u'foursquareapi_venue', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('lat', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('lon', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('foursqueare_url', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('categorie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foursquareapi.Categorie'])),
            ('zone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foursquareapi.Zone'])),
        ))
        db.send_create_signal(u'foursquareapi', ['Venue'])

        # Adding model 'Checkin'
        db.create_table(u'foursquareapi_checkin', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foursquareapi.User'])),
            ('venue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foursquareapi.Venue'])),
            ('num_checkins', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('process', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'foursquareapi', ['Checkin'])


    def backwards(self, orm):
        # Deleting model 'Categorie'
        db.delete_table(u'foursquareapi_categorie')

        # Deleting model 'User'
        db.delete_table(u'foursquareapi_user')

        # Removing M2M table for field friends on 'User'
        db.delete_table('foursquareapi_user_friends')

        # Deleting model 'Zone'
        db.delete_table(u'foursquareapi_zone')

        # Deleting model 'Venue'
        db.delete_table(u'foursquareapi_venue')

        # Deleting model 'Checkin'
        db.delete_table(u'foursquareapi_checkin')


    models = {
        u'foursquareapi.categorie': {
            'Meta': {'object_name': 'Categorie'},
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
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
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
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
            'foursqueare_url': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'lon': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
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