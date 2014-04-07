# -*- coding: utf8 -*- 

from django.db import models
from django.db.models import Q

from smart_selects.db_fields import ChainedForeignKey
from cities_light.models import Country, City

from reference.models import Idioma	
 




# Choices


EMAIL_AE = (
        ('O', 'Oficial'),
        ('A', 'Alternatiu'),
        ('C', 'Coordinador'),
        ('S', 'Secretari'),
        ('T', 'Tresorer'),
    )

# Create your models here.

class Carrec_Ae(models.Model):
    nom = models.CharField(max_length=255)
    descripcio = models.TextField()
    def __unicode__(self): 
    	return self.nom 
    class Meta:
		ordering = ['id']
		verbose_name = "Càrrec de les AE"
		verbose_name_plural = "Càrrecs de les AE"


class Ae(models.Model):
	# tipus = models.IntegerField(choices=AE_TIPUS)
	nom = models.CharField(max_length=50, verbose_name="Nom", help_text="En la llengua originària del país")
	nom_ca = models.CharField(max_length=50, verbose_name="Nom en català")
	nom_en = models.CharField(max_length=50, verbose_name="Nom en anglès")
	estat =  models.ForeignKey(Country, verbose_name="Estat")
	constitucio = models.BooleanField(verbose_name="Constitució")
	data_constitucio = models.DateField(blank=True, null=True, verbose_name="Data constitució")
	acta_constitucio = models.FileField(upload_to='ae/actes_constitucio', blank = True, null = True, verbose_name="Acta constitució")
	activitat = models.BooleanField(default=True,verbose_name="Activa")
	email = models.CharField(max_length=50)
	facebook = models.CharField(max_length=150, blank=True)
	twitter = models.CharField(max_length=30, blank=True)
	web = models.CharField(max_length=150, blank=True)
	data_entrada = models.DateTimeField(auto_now_add=True,
	verbose_name="Data entrada")
	data_actualitzacio = models.DateTimeField(auto_now=True, verbose_name="Darrera actualització")
	def __unicode__(self):
		return self.nom_ca
	class Meta:
		ordering = ['nom_ca']
		verbose_name = "Assemblea Exterior"
		verbose_name_plural = "Assemblees Exteriors"


class GrupLocal(models.Model):
	pass


class EmailAe(models.Model):
	email = models.CharField(max_length=50, verbose_name = "adreça email", unique=True)
	ae = models.ForeignKey(Ae, verbose_name = "AE")
	tipus = models.CharField(max_length=1, choices=EMAIL_AE, verbose_name = "Tipus d'adreça email")
	def __unicode__(self):
		return self.email
	class Meta:
		ordering = ['ae']
		verbose_name = "Email de l'AE"
		verbose_name_plural = "Emails de les AE"
