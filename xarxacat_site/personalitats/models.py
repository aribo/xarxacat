# -*- coding: utf8 -*- 

from django.db import models

from django.contrib.auth.models import User

from smart_selects.db_fields import ChainedForeignKey
from cities_light.models import City, Country

from core.actions import export_as_csv_action
from core.models import TimeStampedModel

from reference.models import Idioma

# Create your models here.

# Àrea

class Area(models.Model):
	nom = models.CharField(max_length=50)
	descripcio = models.CharField(max_length=255)
	def __unicode__(self):
		return self.nom
	class Meta:
		ordering = ['nom']
		verbose_name = "Àrea"
		verbose_name_plural = "Àrees"

# Organització

class Organitzacio_Tipus(models.Model):
	nom = models.CharField(max_length=50)
	descripcio = models.CharField(max_length=255)
	def __unicode__(self):
		return self.nom
	class Meta:
		ordering = ['nom']
		verbose_name = "Tipus d'organització"
		verbose_name_plural = "Tipus d'organització"

class Organitzacio(TimeStampedModel):
	nom = models.CharField(max_length=50)
	tipus = models.ForeignKey(Organitzacio_Tipus, verbose_name="Tipus")
	idioma = models.ManyToManyField(Idioma, verbose_name="Idioma")
	area = models.ForeignKey(Area, verbose_name="Àrea", null=True, blank=True)
	email = models.CharField(max_length=50, verbose_name="Email")
	telefon = models.CharField(max_length=50, verbose_name="Telèfon", null=True)
	url = models.CharField(max_length=50, verbose_name="Web", blank=True)
	adreca = models.CharField(max_length=255, blank=True, null=True, verbose_name="Adreça")
	codipostal = models.CharField(max_length=20, blank=True, null=True, verbose_name="Codi postal")
	pais = models.ForeignKey(Country, verbose_name="País")
	ciutat = ChainedForeignKey(City,
    	chained_field="pais",
    	chained_model_field="country",
    	show_all=False,
    	auto_choose=True,
    	blank=True, null=True, verbose_name="Ciutat",) 
	created_by = models.ForeignKey(User,verbose_name="Creat per", null=True, blank=True)
	def __unicode__(self): 
		return self.nom
	class Meta:
		ordering = ['nom']
		verbose_name = "Organització"
		verbose_name_plural = "Organització"

class Organitzacio_Nota(models.Model):
	nota = models.CharField(max_length=255)
	organitzacio = models.ForeignKey(Organitzacio)
	
	class Meta:
		verbose_name ="Nota d'organització"
		verbose_name_plural = "Notes d'organització"


# Personalitat


class Personalitat(TimeStampedModel):
	nom = models.CharField(max_length=50)
	cognoms = models.CharField(max_length=100)
	email = models.CharField(max_length=50)
	area = models.ForeignKey(Area, verbose_name="Àrea", null=True, blank=True)
	organitzacio = models.ForeignKey(Organitzacio, verbose_name="Organizació", blank=True, null=True)
	carrec = models.CharField(max_length=100, verbose_name="Càrrec", null=True, blank=True)
	pais_origen = models.ForeignKey(Country, related_name = "paisorigen_set", verbose_name="País d'origen", null=True, blank=True)
	idioma = models.ManyToManyField(Idioma, verbose_name="Idioma")
	telefon_fix = models.CharField(max_length=50, verbose_name="Telèfon fix", blank=True)
	telefon_mob = models.CharField(max_length=50, verbose_name="Telèfon mòbil", blank=True)
	twitter = models.CharField(max_length=50, verbose_name="Twitter", null=True, blank=True)
	skype = models.CharField(max_length=50, verbose_name="Skype", null=True, blank=True)
	adreca = models.CharField(max_length=255, blank=True, null=True, verbose_name="Adreça")
	codipostal = models.CharField(max_length=20, blank=True, null=True, verbose_name="Codi postal")
	pais = models.ForeignKey(Country, related_name = "paisres_set", verbose_name="País")
	ciutat = ChainedForeignKey(City,
    	chained_field="pais",
    	chained_model_field="country",
    	show_all=False,
    	auto_choose=True,
    	blank=True, null=True, verbose_name="Ciutat",)
	created_by = models.ForeignKey(User, verbose_name="Creat per", null=True, blank=True)
	
	def __unicode__(self):
		return u'%s %s' % (self.nom, self.cognoms)
	class Meta:
		ordering = ['nom']
		verbose_name = "Personalitat"
		verbose_name_plural = "Personalitats"

class Personalitat_Nota(models.Model):
	nota = models.CharField(max_length=255)
	periodista = models.ForeignKey(Personalitat)
	
	class Meta:
		verbose_name ="Nota de personalitat"
		verbose_name_plural = "Notes de personalitat"
