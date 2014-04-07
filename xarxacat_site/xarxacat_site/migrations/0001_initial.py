# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'XarxacatUsers'
        db.create_table(u'xarxacat_site_xarxacatusers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'xarxacat_site', ['XarxacatUsers'])


    def backwards(self, orm):
        # Deleting model 'XarxacatUsers'
        db.delete_table(u'xarxacat_site_xarxacatusers')


    models = {
        u'xarxacat_site.xarxacatusers': {
            'Meta': {'ordering': "['nom']", 'object_name': 'XarxacatUsers'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['xarxacat_site']