# -*- coding: utf8 -*- 

from django.db import models

class XarxacatUsers(models.Model):
    nom = models.CharField(max_length=255)
    class Meta:
        ordering = ['nom']