# -*- coding: utf8 -*- 

from django.db import models

from cities_light.models import Country, City

# Create your models here.

class Idioma(models.Model):
	nom = models.CharField(max_length=50, verbose_name = "Nom", help_text = "Nom original")
	nom_en = models.CharField(max_length=50, verbose_name = "Nom anglès", help_text = "Nom en anglès")
	nom_ca = models.CharField(max_length=50, verbose_name = "Nom català", help_text = "Nom en català")
	codi = models.CharField(max_length=2, verbose_name = "Codi")
	def __unicode__(self): 
		return self.nom_en 
	class Meta:
		ordering = ['nom_en']
		verbose_name = "Idioma"
		verbose_name_plural = "Idiomes"

class PaisIdioma(models.Model):
	pais = models.ForeignKey(Country, verbose_name = "País")
	idioma = models.ManyToManyField(Idioma, blank=True, null=True, verbose_name = u'Idioma/es al país' )
	def __unicode__(self): 
		return unicode(self.pais)
	class Meta:
		ordering = ['pais']
		verbose_name = "Idiomes del païs"
		verbose_name_plural = "Idiomes de països"