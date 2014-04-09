# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'XarxacatUsers'
        db.delete_table(u'xarxacat_site_xarxacatusers')


    def backwards(self, orm):
        # Adding model 'XarxacatUsers'
        db.create_table(u'xarxacat_site_xarxacatusers', (
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'xarxacat_site', ['XarxacatUsers'])


    models = {
        
    }

    complete_apps = ['xarxacat_site']