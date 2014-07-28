# -*- coding: utf8 -*- 

from django.db import models
from django.db.models import Q

from smart_selects.db_fields import ChainedForeignKey
from cities_light.models import Country, City

from reference.models import Idioma	
from assemblees.models import Ae, Carrec_Ae, GrupLocal
from consell.models import Carrec_Caec
 




# Choices


# Create your models here.



class Membre_Tipus(models.Model):
    nom = models.CharField(max_length=255)
    descripcio = models.CharField(max_length=255)
    def __unicode__(self): 
    	return self.nom
	class Meta:
		ordering = ['id']
		verbose_name = "Tipus de membre"
		verbose_name_plural = "Tipus de membre"


class Membre(models.Model):
    nom = models.CharField(max_length=50)
    cognom_primer = models.CharField(max_length=50, verbose_name="Primer cognom")
    cognom_segon = models.CharField(blank=True,max_length=50, verbose_name="Segon cognom")
    dni = models.CharField(max_length=20, blank=True, verbose_name="DNI", help_text="NUMLLETRA, 56745301F")
    data_naixement = models.DateField(blank=True, null=True,verbose_name="Data de naixement", help_text="ANY-MES-DIA, 1971-07-24")
    email = models.CharField(max_length=50, unique=True, db_index=True)
    skype = models.CharField(max_length=50, blank=True, null=True)
    twitter = models.CharField(max_length=50, blank=True, null=True)
    telefon = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telèfon")
    ae = models.ForeignKey(Ae, blank=True, null=True, verbose_name="Assemblea Exterior")
    codipostal = models.CharField(max_length=20, blank=True, null=True, verbose_name="Codi postal")
    estat = models.ForeignKey(Country, verbose_name="Estat")
    poblacio_ext = ChainedForeignKey(City,
    	chained_field="estat",
    	chained_model_field="country",
    	show_all=False,
    	auto_choose=True,
    	blank=True, null=True, related_name = 'poblacio_ext_set', verbose_name="Població a l'estranger", help_text="Població a l'estranger on el membre resideix normalment")
    poblacio_cat = models.ForeignKey(City, limit_choices_to=Q(display_name__icontains='Catalonia'),
    	blank=True, null=True, related_name = 'poblacio_cat_set', verbose_name="Població a Catalunya", help_text="Població a Catalunya d'on el membre prové")
    tipus = models.ForeignKey(Membre_Tipus, verbose_name="Tipus", help_text="Tipus de membre")
    registre_anc = models.BooleanField(default=True, verbose_name="Registre ANC")
    pagament = models.BooleanField(default=False, verbose_name="Pagament de quotes")
    data_registre_anc = models.DateField(blank=True, null=True, verbose_name="Data registre a l'ANC", help_text="ANY-MES-DIA, 1971-07-24")
    numero_anc = models.CharField(max_length=10, blank=True, null=True, verbose_name="Número soci ANC")
    sectorial_anc = models.CharField(max_length=50, blank=True, null=True, verbose_name="Sectorial")
    professio = models.CharField(max_length=50, blank=True, null=True, verbose_name="Professió")
    habilitats = models.CharField(max_length=200, blank=True, null=True, help_text="Separar per comes ex. Fotografia, Disseny gràfic")
    carrec_ae = models.ManyToManyField(Carrec_Ae, blank=True, null=True, verbose_name="Càrrec a l'AE" )
    carrec_caec = models.ManyToManyField(Carrec_Caec, blank=True, null=True, verbose_name="Càrrec al CAEC")
    activitat = models.BooleanField(default=True, verbose_name="Actiu")
    data_entrada = models.DateTimeField(auto_now_add=True, verbose_name="Data entrada")
    data_actualitzacio = models.DateTimeField(auto_now=True, verbose_name="Darrera actualització")
    def __unicode__(self): 
        return u'%s %s %s' % (self.nom, 'cognom_primer','cognom_segon')


class Membre_Nota(models.Model):
	nota = models.CharField(max_length=255)
	membre = models.ForeignKey(Membre)
	
	class Meta:
		verbose_name ="Nota de membre"
		verbose_name_plural = "Notes de membre"
