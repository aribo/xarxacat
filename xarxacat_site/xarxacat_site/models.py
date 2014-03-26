from django.db import models

class XarxacatUsers(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        managed = True
        db_table = 'xarxacat_users'
        ordering = ['name'] 
