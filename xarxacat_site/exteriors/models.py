from django.db import models

from dashboard.models import Pais


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
    	
class MembreTipus(models.Model):
    nom = models.CharField(max_length=255)
    descripcio = models.CharField(max_length=255)
    def __unicode__(self): 
    	return self.nom
	class Meta:
        	ordering = ['id'] 


class Membre(models.Model):
    dataentrada = models.DateTimeField()
    nom = models.CharField(max_length=255)
    cognoms = models.CharField(max_length=255)
    dni = models.CharField(max_length=20, blank=True)
    datanaixement = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=255)
    skype = models.CharField(max_length=50, blank=True)
    telefon = models.CharField(max_length=20, blank=True)
    ae = models.ForeignKey(Ae)
    codipostal = models.CharField(max_length=255, blank=True)
    pais = models.ForeignKey(Pais)
    poblacio_ext_id = models.IntegerField()
    poblacio_cat_id = models.IntegerField(blank=True, null=True)
    tipus = models.ForeignKey(MembreTipus)
    registre_anc = models.IntegerField()
    dataregistre_anc = models.DateField(blank=True, null=True)
    numero_anc = models.CharField(max_length=255, blank=True)
    sectorial_anc = models.CharField(max_length=255, blank=True)
    professio = models.CharField(max_length=255, blank=True)
    habilitats = models.CharField(max_length=255, blank=True)
    carrec_ae = models.ForeignKey(CarrecAe)
    carrec_caec = models.CharField(max_length=255, blank=True)
    def __unicode__(self): 
        return self.cognoms
    






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