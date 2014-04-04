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


    def backwards(self, orm):
        # Deleting model 'Idioma'
        db.delete_table(u'reference_idioma')


    models = {
        u'reference.idioma': {
            'Meta': {'ordering': "['nom_ca']", 'object_name': 'Idioma'},
            'codi': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nom_ca': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nom_en': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['reference']