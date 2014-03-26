from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Pais(models.Model):
    cat = models.CharField(max_length=100)
    eng = models.CharField(max_length=100)
    esp = models.CharField(max_length=100)
    extra_int = models.IntegerField()
    extra_text = models.TextField()
    iso3166_1_numeric = models.IntegerField()
    iso3166_1_alfa_2 = models.CharField(max_length=2)
    iso3166_1_alfa_3 = models.CharField(max_length=3)
    gmt = models.FloatField()
    gmt_final = models.FloatField()
    continent = models.IntegerField()
    continent_west_east = models.IntegerField()
    fips = models.CharField(max_length=3)
    capital_cat = models.CharField(max_length=100)
    capital_eng = models.CharField(max_length=100)
    capital_esp = models.CharField(max_length=100)
    km2 = models.IntegerField()
    population = models.IntegerField()
    tld = models.CharField(max_length=3)
    currencycode = models.CharField(max_length=3)
    currencyname = models.CharField(max_length=25)
    phone = models.CharField(max_length=5)
    codpos_format = models.CharField(max_length=25)
    codpos_regex = models.CharField(max_length=25)
    languages = models.CharField(max_length=100)
    geonameid = models.IntegerField()
    neighbours = models.CharField(max_length=100)
    status = models.IntegerField()
    def __unicode__(self): 
    	return self.cat
    class Meta:
        ordering = ['cat']

class RefCiutats(models.Model):
    cit_id = models.IntegerField(primary_key=True)
    cit_name = models.CharField(db_column='cit_Name', max_length=100) # Field name made lowercase.
    cit_countrycode = models.CharField(db_column='cit_CountryCode', max_length=3) # Field name made lowercase.
    cit_countryid = models.IntegerField(db_column='cit_CountryId') # Field name made lowercase.
    cit_countryid_alternatiu = models.IntegerField(db_column='cit_CountryId_Alternatiu') # Field name made lowercase.
    cit_district = models.CharField(db_column='cit_District', max_length=20) # Field name made lowercase.
    cit_population = models.IntegerField(db_column='cit_Population') # Field name made lowercase.
    cit_lat = models.FloatField()
    cit_long = models.FloatField()
    cit_provincia = models.IntegerField()
    cit_comarca = models.IntegerField()
    cit_sinonims = models.CharField(db_column='cit_Sinonims', max_length=100) # Field name made lowercase.
    cit_cat = models.CharField(max_length=100)
    class Meta:
        managed = True
        db_table = 'ref_ciutats'





