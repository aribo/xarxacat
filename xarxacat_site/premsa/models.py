# -*- coding: utf8 -*- 

from django.db import models

from django.contrib.auth.models import User

from smart_selects.db_fields import ChainedForeignKey
from cities_light.models import City, Country

from core.actions import export_as_csv_action
from core.models import TimeStampedModel

from reference.models import Idioma


# Create your models here.

class Area(models.Model):
	nom = models.CharField(max_length=50)
	descripcio = models.CharField(max_length=255)
	def __unicode__(self):
		return self.nom
	class Meta:
		ordering = ['nom']
		verbose_name = "Àrea"
		verbose_name_plural = "Àrees"

# Mitjans

class Mitja_Tipus(models.Model):
	nom = models.CharField(max_length=50)
	descripcio = models.CharField(max_length=255)
	def __unicode__(self):
		return self.nom
	class Meta:
		ordering = ['nom']
		verbose_name = "Tipus de mitja"
		verbose_name_plural = "Tipus de mitjà"

class Mitja(TimeStampedModel):
	nom = models.CharField(max_length=50)
	tipus = models.ForeignKey(Mitja_Tipus, verbose_name="Tipus")
	idioma = models.ManyToManyField(Idioma, verbose_name="Idioma")
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
		verbose_name = "Mitjà"
		verbose_name_plural = "Mitjans"

class Mitja_Nota(models.Model):
	nota = models.CharField(max_length=255)
	mitja = models.ForeignKey(Mitja)
	
	class Meta:
		verbose_name ="Nota de mitjà"
		verbose_name_plural = "Notes de mitjà"


# Agències
		
class Agencia_Tipus(models.Model):
	nom = models.CharField(max_length=50)
	descripcio = models.CharField(max_length=255)
	def __unicode__(self): 
		return self.nom
	class Meta:
		ordering = ['nom']
		verbose_name = "Tipus d'agència"
		verbose_name_plural = "Tipus de agència"

class Agencia(TimeStampedModel):
	nom = models.CharField(max_length=50)
	tipus = models.ForeignKey(Agencia_Tipus, verbose_name="Tipus")
	idioma = models.ManyToManyField(Idioma, verbose_name="Idioma")
	email = models.CharField(max_length=50, verbose_name="Email")
	url = models.CharField(max_length=50, verbose_name="Web", blank=True)
	telefon = models.CharField(max_length=50, verbose_name="Telèfon", null=True)
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
		verbose_name = "Agència"
		verbose_name_plural = "Agències"

class Agencia_Nota(models.Model):
	nota = models.CharField(max_length=255)
	agencia = models.ForeignKey(Agencia)
	
	class Meta:
		verbose_name ="Nota de agència"
		verbose_name_plural = "Notes d'agències"


# Periodistes

class Periodista_Tipus(models.Model):
	nom = models.CharField(max_length=50)
	descripcio = models.CharField(max_length=255)
	def __unicode__(self): 
		return self.nom
	class Meta:
		ordering = ['nom']
		verbose_name = "Tipus de periodista"
		verbose_name_plural = "Tipus de periodista"

class Periodista_Carrec(models.Model):
	nom = models.CharField(max_length=50)
	descripcio = models.CharField(max_length=255)
	def __unicode__(self): 
		return self.nom
	class Meta:
		ordering = ['nom']
		verbose_name = "Càrrec de periodista"
		verbose_name_plural = "Carrecs de periodista"

class Periodista(TimeStampedModel):
	nom = models.CharField(max_length=50)
	cognoms = models.CharField(max_length=100)
	email = models.CharField(max_length=50)
	tipus = models.ForeignKey(Periodista_Tipus, verbose_name="Tipus", null=True, blank=True)
	area = models.ForeignKey(Area, verbose_name="Àrea", null=True, blank=True)
	carrec = models.ForeignKey(Periodista_Carrec, verbose_name="Càrrec", null=True, blank=True)
	pais_origen = models.ForeignKey(Country, related_name = "pais_origen_set", verbose_name="País d'origen", null=True, blank=True)
	idioma = models.ManyToManyField(Idioma, verbose_name="Idioma")
	telefon_fix = models.CharField(max_length=50, verbose_name="Telèfon fix", blank=True)
	telefon_mob = models.CharField(max_length=50, verbose_name="Telèfon mòbil", blank=True)
	twitter = models.CharField(max_length=50, verbose_name="Twitter", null=True, blank=True)
	skype = models.CharField(max_length=50, verbose_name="Skype", null=True, blank=True)
	adreca = models.CharField(max_length=255, blank=True, null=True, verbose_name="Adreça")
	codipostal = models.CharField(max_length=20, blank=True, null=True, verbose_name="Codi postal")
	pais = models.ForeignKey(Country, related_name = "pais_set", verbose_name="País")
	ciutat = ChainedForeignKey(City,
    	chained_field="pais",
    	chained_model_field="country",
    	show_all=False,
    	auto_choose=True,
    	blank=True, null=True, verbose_name="Ciutat",)
	agencia = models.ForeignKey(Agencia, verbose_name="Agència", blank=True, null=True)
	mitja = models.ForeignKey(Mitja, verbose_name="Mitjà", blank=True, null=True)
	created_by = models.ForeignKey(User, verbose_name="Creat per", null=True, blank=True)
	
	def __unicode__(self):
		return u'%s %s' % (self.nom, self.cognoms)
	class Meta:
		ordering = ['nom']
		verbose_name = "Periodista"
		verbose_name_plural = "Periodistes"

class Periodista_Nota(models.Model):
	nota = models.CharField(max_length=255)
	periodista = models.ForeignKey(Periodista)
	
	class Meta:
		verbose_name ="Nota de periodista"
		verbose_name_plural = "Notes de periodista"

'''

class Mitja(models.Model):

# to be implemented: "note"
	
class Agencia(models.Model):

# to be implemented: "note"

class Periodista(models.Model):
# to be implemented: "seccio", "programa", "contacte"
	
class SeccioTipus(models.Model):
	nom = models.CharField(max_length=50)
	descripcio = models.CharField(max_length=150)
	
class SeccioMitja(models.Model):
	mitja
	tipus
	email
	telefon
	
class Programa(models.Model):
	nom = models.CharField(max_length=50)
	mitja
	tipus
	idioma
	contacte
	email
	telefon
	nota = models.CharField(max_length=50)
	created_by
	data_entrada
	data_actualitzacio
	
class Contacte(models.Model):
	titol = models.CharField(max_length=50)
	descripcio
	origen
	resultat
	created_by
	data_entrada
	data_actualitzacio

class Notes(models.Model):
	nota
	autor
	created_by
	data_entrada
	data_actualitzacio
	
- Tipus possibles de Mitjà
Diaris, Revistes, Mitjans Digitals, Agència, Ràdio, TV, Blog.

- Tipus possibles d'Agència?
No se si caldria.... en tot cas opcions que es podrien: premsa, foto,
video. Però en molts casos les agències son dels 3 tipus, no?

- Tipus possibles de Periodista
bo, dolent, nefast, unionista... oh, wait... segurament no volies dir això. : )
De tipus, doncs depèn el que volgueu dir amb aquest camp: et
refereixes a la tipologia de mitja en el qual treballa? premsa, radio,
tv...
o més aviat al "càrrec" que ocupa dins del mitjà. Redactor, Editor,
Redactor en cap, Cap de Secció, director, sotsdirector o hauria de
quedar-hi reflectida la secció del mitjà en què treballa: politica,
economia, Internacional, Europa?

'''