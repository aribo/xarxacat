# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Membre_Tipus'
        db.create_table(u'membres_membre_tipus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('descripcio', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'membres', ['Membre_Tipus'])

        # Adding model 'Membre'
        db.create_table(u'membres_membre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cognoms', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('dni', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('data_naixement', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50, db_index=True)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('telefon', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('ae', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['assemblees.Ae'], null=True, blank=True)),
            ('codipostal', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('estat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.Country'])),
            ('poblacio_ext', self.gf('smart_selects.db_fields.ChainedForeignKey')(blank=True, related_name='poblacio_ext_set', null=True, to=orm['cities_light.City'])),
            ('poblacio_cat', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='poblacio_cat_set', null=True, to=orm['cities_light.City'])),
            ('tipus', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['membres.Membre_Tipus'])),
            ('registre_anc', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('pagament', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_registre_anc', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('numero_anc', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('sectorial_anc', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('professio', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('habilitats', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('activitat', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('data_entrada', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_actualitzacio', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'membres', ['Membre'])

        # Adding M2M table for field carrec_ae on 'Membre'
        m2m_table_name = db.shorten_name(u'membres_membre_carrec_ae')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membre', models.ForeignKey(orm[u'membres.membre'], null=False)),
            ('carrec_ae', models.ForeignKey(orm[u'assemblees.carrec_ae'], null=False))
        ))
        db.create_unique(m2m_table_name, ['membre_id', 'carrec_ae_id'])

        # Adding M2M table for field carrec_caec on 'Membre'
        m2m_table_name = db.shorten_name(u'membres_membre_carrec_caec')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membre', models.ForeignKey(orm[u'membres.membre'], null=False)),
            ('carrec_caec', models.ForeignKey(orm[u'consell.carrec_caec'], null=False))
        ))
        db.create_unique(m2m_table_name, ['membre_id', 'carrec_caec_id'])


    def backwards(self, orm):
        # Deleting model 'Membre_Tipus'
        db.delete_table(u'membres_membre_tipus')

        # Deleting model 'Membre'
        db.delete_table(u'membres_membre')

        # Removing M2M table for field carrec_ae on 'Membre'
        db.delete_table(db.shorten_name(u'membres_membre_carrec_ae'))

        # Removing M2M table for field carrec_caec on 'Membre'
        db.delete_table(db.shorten_name(u'membres_membre_carrec_caec'))


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
            'cognoms': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
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