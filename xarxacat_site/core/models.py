# -*- coding: utf8 -*- 

from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):
	"""
	An abstract base class model that
	provides self-updating ’date_created’
	and ’date_modified’ fields.
	"""
	date_created = models.DateTimeField(
				auto_now_add=True, verbose_name="Data entrada")
	date_modified = models.DateTimeField(
				auto_now=True, verbose_name="Darrera actualització")
	class Meta:
		abstract = True
