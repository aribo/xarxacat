# -*- coding: utf8 -*- 

from django.db import models
from django.db.models import Q

from smart_selects.db_fields import ChainedForeignKey
from cities_light.models import Country, City
 




# Choices
	

# Create your models here.

    	

class Carrec_Ae(models.Model):
    nom = models.CharField(max_length=255)
    descripcio = models.TextField()
    def __unicode__(self): 
    	return self.nom 
    class Meta:
		ordering = ['id']
		verbose_name = "Carrec de les AE"
		verbose_name_plural = "Carrecs de les AE"  

class Carrec_Caec(models.Model):
    nom = models.CharField(max_length=255)
    descripcio = models.TextField()
    def __unicode__(self): 
    	return self.nom 
    class Meta:
		ordering = ['id']
		verbose_name = "Carrec del CAEC"
		verbose_name_plural = "Carrecs del CAEC"

class Membre_Tipus(models.Model):
    nom = models.CharField(max_length=255)
    descripcio = models.CharField(max_length=255)
    def __unicode__(self): 
    	return self.nom
	class Meta:
		ordering = ['id']
		verbose_name = "Tipus de membre"
		verbose_name_plural = "Tipus de membre"
		

class Ae(models.Model):
	# tipus = models.IntegerField(choices=AE_TIPUS)
	nom = models.CharField(max_length=50, verbose_name="Nom", help_text="En la llengua originària del país")
	nom_ca = models.CharField(max_length=50, verbose_name="Nom en català")
	nom_en = models.CharField(max_length=50, verbose_name="Nom en anglès")
	estat =  models.ForeignKey(Country, verbose_name="Estat")
	constitucio = models.BooleanField(verbose_name="Constitució")
	data_constitucio = models.DateField(blank=True, null=True, verbose_name="Data constitució")
	activitat = models.BooleanField(default=True,verbose_name="Activitat", help_text="Indicar si l'AE està activa")
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


class Membre(models.Model):
    nom = models.CharField(max_length=50)
    cognoms = models.CharField(max_length=50)
    dni = models.CharField(max_length=20, blank=True, verbose_name="DNI", help_text="NUMLLETRA, 56745301F")
    data_naixement = models.DateField(blank=True, null=True,verbose_name="Data de naixement", help_text="ANY-MES-DIA, 1971-07-24")
    email = models.CharField(max_length=50)
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
    registre_anc = models.NullBooleanField(default=True, verbose_name="Registre ANC")
    pagament = models.NullBooleanField(default=False, verbose_name="Pagament de quotes")
    data_registre_anc = models.DateField(blank=True, null=True, verbose_name="Data registre a l'ANC", help_text="ANY-MES-DIA, 1971-07-24")
    numero_anc = models.CharField(max_length=10, blank=True, null=True, verbose_name="Número soci ANC")
    sectorial_anc = models.CharField(max_length=50, blank=True, null=True, verbose_name="Sectorial")
    professio = models.CharField(max_length=50, blank=True, null=True, verbose_name="Professió")
    habilitats = models.CharField(max_length=200, blank=True, null=True, help_text="Separar per comes ex. Fotografia, Disseny gràfic")
    carrec_ae = models.ManyToManyField(Carrec_Ae, blank=True, null=True, verbose_name="Càrrec a l'AE" )
    carrec_caec = models.ManyToManyField(Carrec_Caec, blank=True, null=True, verbose_name="Càrrec al CAEC")
    actiu = models.BooleanField(default=True, verbose_name="Actiu", help_text = "Indica si el membre té encara relació amb l'ANC")
    data_entrada = models.DateTimeField(auto_now_add=True, verbose_name="Data entrada")
    data_actualitzacio = models.DateTimeField(auto_now=True, verbose_name="Darrera actualització")
    def __unicode__(self): 
        return u'%s %s' % (self.nom, self.cognoms)
 
'''
    dni = CharField()
    data_naixement = DateField()
    email = CharField()
    skype = CharField()
    telefon = CharField()
    ae = IntegerField()
    codipostal = CharField()
    estat = IntegerField()
    poblacio_ext = IntegerField()
    poblacio_cat = IntegerField()
    tipus = IntegerField()
    registre_anc = IntegerField()
    pagament = IntegerField()
    data_registre_anc = DateField()
    numero_anc = CharField()
    sectorial_anc = CharField()
    professio = CharField()
    habilitats = CharField()
    data_entrada = DateTimeField()
    data_actualitzacio = DateTimeField()
    '''
	
	



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