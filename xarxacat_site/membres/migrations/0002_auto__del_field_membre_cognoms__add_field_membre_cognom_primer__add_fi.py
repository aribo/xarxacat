# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Membre.cognoms'
        db.delete_column(u'membres_membre', 'cognoms')

        # Adding field 'Membre.cognom_primer'
        db.add_column(u'membres_membre', 'cognom_primer',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Membre.cognom_segon'
        db.add_column(u'membres_membre', 'cognom_segon',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Membre.cognoms'
        db.add_column(u'membres_membre', 'cognoms',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Deleting field 'Membre.cognom_primer'
        db.delete_column(u'membres_membre', 'cognom_primer')

        # Deleting field 'Membre.cognom_segon'
        db.delete_column(u'membres_membre', 'cognom_segon')


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
        u'cities_light.city': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('region', 'name'),)", 'object_name': 'City'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Country']"}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'feature_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'population': ('django.db.models.fields.BigIntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Region']", 'null': 'True', 'blank': 'True'}),
            'search_names': ('cities_light.models.ToSearchTextField', [], {'default': "''", 'max_length': '4000', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"})
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
        },
        u'cities_light.region': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('country', 'name'),)", 'object_name': 'Region'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Country']"}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'geoname_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"})
        },
        u'consell.carrec_caec': {
            'Meta': {'ordering': "['id']", 'object_name': 'Carrec_Caec'},
            'descripcio': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'membres.membre': {
            'Meta': {'object_name': 'Membre'},
            'activitat': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ae': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['assemblees.Ae']", 'null': 'True', 'blank': 'True'}),
            'carrec_ae': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['assemblees.Carrec_Ae']", 'null': 'True', 'blank': 'True'}),
            'carrec_caec': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['consell.Carrec_Caec']", 'null': 'True', 'blank': 'True'}),
            'codipostal': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'cognom_primer': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cognom_segon': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'data_actualitzacio': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_entrada': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_naixement': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'data_registre_anc': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'dni': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'estat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Country']"}),
            'habilitats': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'numero_anc': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'pagament': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'poblacio_cat': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'poblacio_cat_set'", 'null': 'True', 'to': u"orm['cities_light.City']"}),
            'poblacio_ext': ('smart_selects.db_fields.ChainedForeignKey', [], {'blank': 'True', 'related_name': "'poblacio_ext_set'", 'null': 'True', 'to': u"orm['cities_light.City']"}),
            'professio': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'registre_anc': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sectorial_anc': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'telefon': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'tipus': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['membres.Membre_Tipus']"}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'membres.membre_tipus': {
            'Meta': {'object_name': 'Membre_Tipus'},
            'descripcio': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['membres']