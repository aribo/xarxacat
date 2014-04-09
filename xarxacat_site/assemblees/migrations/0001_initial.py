# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Carrec_Ae'
        db.create_table(u'assemblees_carrec_ae', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('descripcio', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'assemblees', ['Carrec_Ae'])

        # Adding model 'Ae'
        db.create_table(u'assemblees_ae', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('nom_ca', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('nom_en', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('estat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.Country'])),
            ('constitucio', self.gf('django.db.models.fields.BooleanField')()),
            ('data_constitucio', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('acta_constitucio', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('activitat', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('facebook', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('web', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('data_entrada', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_actualitzacio', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'assemblees', ['Ae'])

        # Adding model 'GrupLocal'
        db.create_table(u'assemblees_gruplocal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'assemblees', ['GrupLocal'])

        # Adding model 'EmailAe'
        db.create_table(u'assemblees_emailae', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('ae', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['assemblees.Ae'])),
            ('tipus', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'assemblees', ['EmailAe'])


    def backwards(self, orm):
        # Deleting model 'Carrec_Ae'
        db.delete_table(u'assemblees_carrec_ae')

        # Deleting model 'Ae'
        db.delete_table(u'assemblees_ae')

        # Deleting model 'GrupLocal'
        db.delete_table(u'assemblees_gruplocal')

        # Deleting model 'EmailAe'
        db.delete_table(u'assemblees_emailae')


    models = {
        u'assemblees.ae': {
            'Meta': {'ordering': "['nom_ca']", 'object_name': 'Ae'},
            'acta_constitucio': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'activitat': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'constitucio': ('django.db.models.fields.BooleanField', [], {}),
            'data_actualitzacio': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_constitucio': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'data_entrada': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'estat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Country']"}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nom_ca': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nom_en': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'web': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'})
        },
        u'assemblees.carrec_ae': {
            'Meta': {'ordering': "['id']", 'object_name': 'Carrec_Ae'},
            'descripcio': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'assemblees.emailae': {
            'Meta': {'ordering': "['ae']", 'object_name': 'EmailAe'},
            'ae': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['assemblees.Ae']"}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipus': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'assemblees.gruplocal': {
            'Meta': {'object_name': 'GrupLocal'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'cities_light.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'code2': ('django.db.models.fields.CharField', [], {'max_length': '2', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'code3': ('django.db.models.fields.CharField', [], {'max_length': '3', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'continent': ('django.db.models.fields.CharField', [], {'max_length': '2', 'db_index': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"}),
            'tld': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '5', 'blank': 'True'})
        }
    }

    complete_apps = ['assemblees']