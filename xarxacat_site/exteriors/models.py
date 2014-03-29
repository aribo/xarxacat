# -*- coding: utf8 -*- 

from django.db import models
from django.db.models import Q

from cities_light.models import Country, City

from smart_selects.db_fields import ChainedForeignKey 


# Choices

AE_TIPUS = (
	(1, 'Nacional'),
	(2, 'Local'),
	(3, 'Regional'),
	)
CONSTITUCIO = (
	(1, 'Sí'),
	(2, 'No'),
	(3, 'En procés'),
	)
	

# Create your models here.

    	
class Carrec_Ae(models.Model):
    nom = models.CharField(max_length=255)
    descripcio = models.TextField()
    def __unicode__(self): 
    	return self.nom 
	class Meta:
        	ordering = ['id'] 
        	
        	
class Carrec_Caec(models.Model):
    nom = models.CharField(max_length=255)
    descripcio = models.TextField()
    def __unicode__(self): 
    	return self.nom 
	class Meta:
        	ordering = ['id']      	
    	
class Membre_Tipus(models.Model):
    nom = models.CharField(max_length=255)
    descripcio = models.CharField(max_length=255)
    def __unicode__(self): 
    	return self.nom
	class Meta:
        	ordering = ['id'] 

class Ae(models.Model):
	# tipus = models.IntegerField(choices=AE_TIPUS)
	nom = models.CharField(max_length=50, verbose_name="Nom", help_text="En la llengua originària del país")
	nom_ca = models.CharField(max_length=50, verbose_name="Nom en català")
	nom_en = models.CharField(max_length=50, verbose_name="Nom en anglès")
	estat =  models.ForeignKey(Country, verbose_name="Estat")
	constitucio = models.IntegerField(choices=CONSTITUCIO, verbose_name="Constitució")
	data_constitucio = models.DateField(blank=True, null=True, verbose_name="Data constitució")
	activitat = models.BooleanField(default=True,verbose_name="Activitat", help_text="Indicar si l'AE està activa")
	email = models.CharField(max_length=50)
	facebook = models.CharField(max_length=150, blank=True)
	twitter = models.CharField(max_length=30, blank=True)
	web = models.CharField(max_length=150, blank=True)
	data_entrada = models.DateTimeField(#auto_now_add=True,
	verbose_name="Data entrada")
	data_actualitzacio = models.DateTimeField(auto_now=True, verbose_name="Darrera actualització")
	def __unicode__(self):
		return self.nom_ca
	class Meta:
		ordering = ['nom_ca']
		verbose_name = "Assemblea Exterior"
		verbose_name_plural = "Assemblees Exteriors"


class Membre(models.Model):
    nom = models.CharField(max_length=50)
    cognoms = models.CharField(max_length=50)
    dni = models.CharField(max_length=20, blank=True, verbose_name="DNI")
    datanaixement = models.DateField(blank=True, null=True, verbose_name="Data de naixement")
    email = models.CharField(max_length=50)
    skype = models.CharField(max_length=50, blank=True)
    telefon = models.CharField(max_length=20, blank=True, verbose_name="Telèfon")
    ae = models.ForeignKey(Ae, blank=True, null=True, verbose_name="Assemblea Exterior")
    codipostal = models.CharField(max_length=20, blank=True, verbose_name="Codi postal")
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
    registre_anc = models.NullBooleanField(default=True,verbose_name="Registre ANC")
    pagament = models.NullBooleanField(default=False,verbose_name="Pagament de quotes")
    dataregistre_anc = models.DateField(blank=True, null=True, verbose_name="Data registre a l'ANC")
    numero_anc = models.CharField(max_length=255, blank=True, verbose_name="Número soci ANC")
    sectorial_anc = models.CharField(max_length=255, blank=True, verbose_name="Sectorial")
    professio = models.CharField(max_length=255, blank=True, verbose_name="Professió")
    habilitats = models.CharField(max_length=255, blank=True)
    carrec_ae = models.ForeignKey(Carrec_Ae, blank=True, null=True, verbose_name="Càrrec a l'AE", help_text="Si el membre té un càrrec a la seva AE, si no deixar buit")
    carrec_caec = models.ForeignKey(Carrec_Caec, blank=True, null=True, verbose_name="Càrrec al CAEC",  help_text="Si el membre té un càrrec al Consell, si no deixar buit")
    data_entrada = models.DateTimeField(auto_now_add=True, verbose_name="Data entrada")
    data_actualitzacio = models.DateTimeField(auto_now=True, verbose_name="Darrera actualització")
    def __unicode__(self): 
        return u'%s %s' % (self.nom, self.cognoms)

   


###

'''
class NotaMembre(models.Model):
    membre_id = models.ForeignKey(Membre)
    nota = models.CharField(max_length=255)
    class Meta:
        managed = True
        db_table = 'ancext_membres_notes'



class AncextProjectes(models.Model):
    projecte_id = models.IntegerField(primary_key=True)
    projecte_nom = models.CharField(max_length=255)
    projecte_hashname = models.CharField(max_length=255)
    projecte_descripcio = models.TextField()
    class Meta:
        managed = True
        db_table = 'ancext_projectes'

class AncextProjectesMembres(models.Model):
    projectes_membres_id = models.IntegerField(primary_key=True)
    projecte_id = models.IntegerField()
    membre_id = models.IntegerField()
    class Meta:
        managed = True
        db_table = 'ancext_projectes_membres'
'''