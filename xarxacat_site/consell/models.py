from django.db import models

# Create your models here.

class Carrec_Caec(models.Model):
    nom = models.CharField(max_length=255)
    descripcio = models.TextField()
    def __unicode__(self): 
    	return self.nom 
    class Meta:
		ordering = ['id']
		verbose_name = "Carrec del CAEC"
		verbose_name_plural = "Carrecs del CAEC"
