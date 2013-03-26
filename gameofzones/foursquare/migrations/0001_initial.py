# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Categorie'
        db.create_table(u'foursquare_categorie', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=30, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('icon', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'foursquare', ['Categorie'])

        # Adding model 'User'
        db.create_table(u'foursquare_user', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=30, primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
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
        db.send_create_signal(u'foursquare', ['User'])

        # Adding M2M table for field friends on 'User'
        db.create_table(u'foursquare_user_friends', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_user', models.ForeignKey(orm[u'foursquare.user'], null=False)),
            ('to_user', models.ForeignKey(orm[u'foursquare.user'], null=False))
        ))
        db.create_unique(u'foursquare_user_friends', ['from_user_id', 'to_user_id'])

        # Adding model 'Zone'
        db.create_table(u'foursquare_zone', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('king', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foursquare.User'])),
            ('num_venues', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'foursquare', ['Zone'])

        # Adding model 'Venue'
        db.create_table(u'foursquare_venue', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=30, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('lat', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('lon', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('foursquare_url', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('categorie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foursquare.Categorie'])),
            ('zone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foursquare.Zone'])),
        ))
        db.send_create_signal(u'foursquare', ['Venue'])

        # Adding model 'Checkin'
        db.create_table(u'foursquare_checkin', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foursquare.User'])),
            ('venue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foursquare.Venue'])),
            ('num_checkins', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('process', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'foursquare', ['Checkin'])


    def backwards(self, orm):
        # Deleting model 'Categorie'
        db.delete_table(u'foursquare_categorie')

        # Deleting model 'User'
        db.delete_table(u'foursquare_user')

        # Removing M2M table for field friends on 'User'
        db.delete_table('foursquare_user_friends')

        # Deleting model 'Zone'
        db.delete_table(u'foursquare_zone')

        # Deleting model 'Venue'
        db.delete_table(u'foursquare_venue')

        # Deleting model 'Checkin'
        db.delete_table(u'foursquare_checkin')


    models = {
        u'foursquare.categorie': {
            'Meta': {'object_name': 'Categorie'},
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35'})
        },
        u'foursquare.checkin': {
            'Meta': {'object_name': 'Checkin'},
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
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'friends_rel_+'", 'to': u"orm['foursquare.User']"}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'num_friends': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'num_zones': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'photo': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'foursquare.venue': {
            'Meta': {'object_name': 'Venue'},
            'categorie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['foursquare.Categorie']"}),
            'checkins': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['foursquare.User']", 'through': u"orm['foursquare.Checkin']", 'symmetrical': 'False'}),
            'foursquare_url': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'lon': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['foursquare.Zone']"})
        },
        u'foursquare.zone': {
            'Meta': {'object_name': 'Zone'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'king': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['foursquare.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'num_venues': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['foursquare']