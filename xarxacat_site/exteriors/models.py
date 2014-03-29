# -*- coding: utf8 -*- 

from django.db import models

from cities_light.models import Country, City

from smart_selects.db_fields import ChainedForeignKey 


# Create your models here.

class Ae(models.Model):
    tipus = models.CharField(max_length=255)
    area_ca = models.CharField(max_length=100)
    area_en = models.CharField(max_length=100)
    area_lang = models.CharField(max_length=100)
    country = models.IntegerField(blank=True, null=True)
    constitution = models.IntegerField()
    active = models.IntegerField()
    constitution_date = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=100)
    facebook = models.CharField(max_length=255, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    web = models.CharField(max_length=255, blank=True)
    def __unicode__(self): 
    	return self.area_ca
	class Meta:
       		ordering = ['area_ca']
    	
class CarrecAe(models.Model):
    nom = models.CharField(max_length=255)
    descripcio = models.TextField()
    def __unicode__(self): 
    	return self.nom 
	class Meta:
        	ordering = ['id'] 
        	
class CarrecCaec(models.Model):
    nom = models.CharField(max_length=255)
    descripcio = models.TextField()
    def __unicode__(self): 
    	return self.nom 
	class Meta:
        	ordering = ['id']      	
    	
class MembreTipus(models.Model):
    nom = models.CharField(max_length=255)
    descripcio = models.CharField(max_length=255)
    def __unicode__(self): 
    	return self.nom
	class Meta:
        	ordering = ['id'] 

class RegistreAnc(models.Model):
	label = models.CharField(max_length=4)
	def __unicode__(self):
		return self.label
		
class Pagament(models.Model):
	status = models.CharField(max_length=10)
	def __unicode__(self):
		return self.status
	


class Membre(models.Model):
    dataentrada = models.DateTimeField(verbose_name="Data entrada")
    nom = models.CharField(max_length=255)
    cognoms = models.CharField(max_length=255)
    dni = models.CharField(max_length=20, blank=True, verbose_name="DNI")
    datanaixement = models.DateField(blank=True, null=True, verbose_name="Data de naixement")
    email = models.CharField(max_length=255)
    skype = models.CharField(max_length=50, blank=True)
    telefon = models.CharField(max_length=20, blank=True, verbose_name="Telèfon")
    ae = models.ForeignKey(Ae, verbose_name="Assemblea Exterior")
    codipostal = models.CharField(max_length=255, blank=True, verbose_name="Codi postal")
    estat = models.ForeignKey(Country)
    poblacio_ext = ChainedForeignKey(City,
    	chained_field="pais",
    	chained_model_field="country",
    	show_all=False,
    	auto_choose=True,
    	blank=True, null=True, related_name = 'poblacio_ext_set', verbose_name="Població a l'estranger", help_text="Població a l'estranger on el membre resideix normalment")
    poblacio_cat = models.ForeignKey(City, limit_choices_to={'region_id': 921},
    	blank=True, null=True, related_name = 'poblacio_cat_set', verbose_name="Població a Catalunya", help_text="Població a Catalunya d'on el membre prové")
    tipus = models.ForeignKey(MembreTipus, help_text="Tipus de membre")
    registre_anc = models.ForeignKey(RegistreAnc, verbose_name="Registre ANC")
    pagament = models.ForeignKey(Pagament, default="Corrent")
    dataregistre_anc = models.DateField(blank=True, null=True, verbose_name="Data registre a l'ANC")
    numero_anc = models.CharField(max_length=255, blank=True, verbose_name="Número soci ANC")
    sectorial_anc = models.CharField(max_length=255, blank=True, verbose_name="Sectorial")
    professio = models.CharField(max_length=255, blank=True, verbose_name="Professió")
    habilitats = models.CharField(max_length=255, blank=True)
    carrec_ae = models.ForeignKey(CarrecAe, blank=True, null=True, verbose_name="Càrrec a l'AE", help_text="Si el membre té un càrrec a la seva AE, si no deixar buit")
    carrec_caec = models.ForeignKey(CarrecCaec, blank=True, null=True, verbose_name="Càrrec al CAEC",  help_text="Si el membre té un càrrec al Consell, si no deixar buit")
    def __unicode__(self): 
        return u'%s %s' % (self.nom, self.cognoms)
   


###


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