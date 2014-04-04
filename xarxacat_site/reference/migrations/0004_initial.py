# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Idioma'
        db.create_table(u'reference_idioma', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('nom_en', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('nom_ca', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('codi', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'reference', ['Idioma'])

        # Adding model 'PaisIdioma'
        db.create_table(u'reference_paisidioma', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.Country'])),
        ))
        db.send_create_signal(u'reference', ['PaisIdioma'])

        # Adding M2M table for field idioma on 'PaisIdioma'
        m2m_table_name = db.shorten_name(u'reference_paisidioma_idioma')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('paisidioma', models.ForeignKey(orm[u'reference.paisidioma'], null=False)),
            ('idioma', models.ForeignKey(orm[u'reference.idioma'], null=False))
        ))
        db.create_unique(m2m_table_name, ['paisidioma_id', 'idioma_id'])


    def backwards(self, orm):
        # Deleting model 'Idioma'
        db.delete_table(u'reference_idioma')

        # Deleting model 'PaisIdioma'
        db.delete_table(u'reference_paisidioma')

        # Removing M2M table for field idioma on 'PaisIdioma'
        db.delete_table(db.shorten_name(u'reference_paisidioma_idioma'))


    models = {
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
        u'reference.idioma': {
            'Meta': {'ordering': "['nom_en']", 'object_name': 'Idioma'},
            'codi': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nom_ca': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nom_en': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'reference.paisidioma': {
            'Meta': {'ordering': "['pais']", 'object_name': 'PaisIdioma'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idioma': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['reference.Idioma']", 'null': 'True', 'blank': 'True'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Country']"})
        }
    }

    complete_apps = ['reference']