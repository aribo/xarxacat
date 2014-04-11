# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Periodista.telefon_mob'
        db.alter_column(u'premsa_periodista', 'telefon_mob', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Periodista.telefon_fix'
        db.alter_column(u'premsa_periodista', 'telefon_fix', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

    def backwards(self, orm):

        # Changing field 'Periodista.telefon_mob'
        db.alter_column(u'premsa_periodista', 'telefon_mob', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Periodista.telefon_fix'
        db.alter_column(u'premsa_periodista', 'telefon_fix', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'premsa.agencia': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Agencia'},
            'adreca': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ciutat': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['cities_light.City']", 'null': 'True', 'blank': 'True'}),
            'codipostal': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idioma': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['reference.Idioma']", 'symmetrical': 'False'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Country']"}),
            'telefon': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'tipus': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['premsa.Agencia_Tipus']"})
        },
        u'premsa.agencia_tipus': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Agencia_Tipus'},
            'descripcio': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'premsa.mitja': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Mitja'},
            'adreca': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ciutat': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['cities_light.City']", 'null': 'True', 'blank': 'True'}),
            'codipostal': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idioma': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['reference.Idioma']", 'symmetrical': 'False'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Country']"}),
            'telefon': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'tipus': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['premsa.Mitja_Tipus']"})
        },
        u'premsa.mitja_tipus': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Mitja_Tipus'},
            'descripcio': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'premsa.periodista': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Periodista'},
            'adreca': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'agencia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['premsa.Agencia']", 'null': 'True', 'blank': 'True'}),
            'carrec': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['premsa.Periodista_Carrec']", 'null': 'True', 'blank': 'True'}),
            'ciutat': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['cities_light.City']", 'null': 'True', 'blank': 'True'}),
            'codipostal': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'cognoms': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idioma': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['reference.Idioma']", 'symmetrical': 'False'}),
            'mitja': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['premsa.Mitja']", 'null': 'True', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pais_set'", 'to': u"orm['cities_light.Country']"}),
            'pais_origen': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'pais_origen_set'", 'null': 'True', 'to': u"orm['cities_light.Country']"}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'telefon_fix': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'telefon_mob': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'tipus': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['premsa.Periodista_Tipus']", 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'premsa.periodista_carrec': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Periodista_Carrec'},
            'descripcio': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'premsa.periodista_tipus': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Periodista_Tipus'},
            'descripcio': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'reference.idioma': {
            'Meta': {'ordering': "['nom_en']", 'object_name': 'Idioma'},
            'codi': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nom_ca': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nom_en': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['premsa']