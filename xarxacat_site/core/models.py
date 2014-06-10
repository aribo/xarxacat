# -*- coding: utf8 -*- 

from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):
	"""
	An abstract base class model that
	provides self-updating ’date_created’
	and ’date_modified’ fields.
	"""
	created_at = models.DateTimeField(
				auto_now_add=True, verbose_name="Data entrada")
	updated_at = models.DateTimeField(
				auto_now=True, verbose_name="Darrera actualització")
	class Meta:
		abstract = True