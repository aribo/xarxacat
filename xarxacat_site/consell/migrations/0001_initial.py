# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Carrec_Caec'
        db.create_table(u'consell_carrec_caec', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('descripcio', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'consell', ['Carrec_Caec'])


    def backwards(self, orm):
        # Deleting model 'Carrec_Caec'
        db.delete_table(u'consell_carrec_caec')


    models = {
        u'consell.carrec_caec': {
            'Meta': {'ordering': "['id']", 'object_name': 'Carrec_Caec'},
            'descripcio': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['consell']