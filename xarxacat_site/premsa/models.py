# -*- coding: utf8 -*- 

from django.db import models

# Create your models here.

'''

class Mitja(models.Model):
	nom = models.CharField(max_length=50)
	pais
	tipus
	idioma
	email = models.CharField(max_length=50)
	telefon
	adreca
	codipostal = models.CharField(max_length=50)
	pais
	ciutat
	nota
	created_by
	data_entrada
	data_actualitzacio
	
class Agencia(models.Model):
	nom = models.CharField(max_length=50)
	pais
	tipus
	idioma
	email = models.CharField(max_length=50)
	telefon
	adreca
	codipostal = models.CharField(max_length=50)
	pais
	ciutat
	nota = models.CharField(max_length=50)
	created_by
	data_entrada
	data_actualitzacio
	
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

class Periodista(models.Model):
	nom = models.CharField(max_length=50)
	cognoms = models.CharField(max_length=100)
	email = models.CharField(max_length=50)
	tipus
	carrec
	seccio
	pais_origen
	idioma
	telefon_fix = models.CharField(max_length=50)
	telefon_mob = models.CharField(max_length=50)
	twitter = models.CharField(max_length=50)
	skype = models.CharField(max_length=50)
	adreca
	codipostal = models.CharField(max_length=50)
	pais
	ciutat
	agencia
	mitja
	programa
	contacte
	nota
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