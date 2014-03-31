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
	nota
	data_entrada
	data_actualitzacio
	
class Agencia(models.Model):
	nom = models.CharField(max_length=50)
	pais
	tipus
	idioma
	email
	nota = models.CharField(max_length=50)
	data_entrada
	data_actualitzacio

class Periodista(models.Model):
	nom = models.CharField(max_length=50)
	cognoms = models.CharField(max_length=100)
	email = models.CharField(max_length=50)
	tipus
	pais_origen
	idioma
	telefon = models.CharField(max_length=50)
	twitter = models.CharField(max_length=50)
	skype = models.CharField(max_length=50)
	adreca
	codipostal = models.CharField(max_length=50)
	pais
	ciutat
	agencia
	mitja
	contacte
	nota
	data_entrada
	data_actualitzacio
	
class Contacte(models.Model):
	titol = models.CharField(max_length=50)
	descripcio
	autor
	resultat
	data_entrada
	data_actualitzacio

class Notes(models.Model):
	nota
	autor
	data_entrada
	data_actualitzacio

'''