from __future__ import unicode_literals

from django.db import models

class AncextAe(models.Model):
    ae_id = models.IntegerField(primary_key=True)
    ae_type = models.CharField(max_length=255)
    ae_area_ca = models.CharField(max_length=100)
    ae_area_en = models.CharField(max_length=100)
    ae_area_lang = models.CharField(max_length=100)
    ae_country = models.IntegerField(blank=True, null=True)
    ae_constitution = models.IntegerField()
    ae_active = models.IntegerField()
    ae_constitution_date = models.DateField(blank=True, null=True)
    ae_email = models.CharField(max_length=100)
    ae_facebook = models.CharField(max_length=255, blank=True)
    ae_twitter = models.CharField(max_length=100, blank=True)
    ae_web = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'ancext_ae'

class AncextAeCarrecs(models.Model):
    ae_carrec_id = models.IntegerField(primary_key=True)
    ae_carrec_nom = models.CharField(max_length=255)
    ae_carrec_descripcio = models.TextField()
    class Meta:
        managed = False
        db_table = 'ancext_ae_carrecs'

class AncextMembres(models.Model):
    membre_id = models.IntegerField(primary_key=True)
    membre_dataentrada = models.DateTimeField()
    membre_nom = models.CharField(max_length=255)
    membre_cognoms = models.CharField(max_length=255)
    membre_dni = models.CharField(max_length=20, blank=True)
    membre_datanaixement = models.DateField(blank=True, null=True)
    membre_email = models.CharField(max_length=255)
    membre_skype = models.CharField(max_length=50, blank=True)
    membre_telefon = models.CharField(max_length=20, blank=True)
    membre_ae_id = models.IntegerField()
    membre_codipostal = models.CharField(max_length=255, blank=True)
    membre_poblacio_ext_id = models.IntegerField()
    membre_poblacio_cat_id = models.IntegerField(blank=True, null=True)
    membre_tipus_id = models.IntegerField()
    membre_registre_anc = models.IntegerField()
    membre_dataregistre_anc = models.DateField(blank=True, null=True)
    membre_numero_anc = models.CharField(max_length=255, blank=True)
    membre_sectorial_anc = models.CharField(max_length=255, blank=True)
    membre_professio = models.CharField(max_length=255, blank=True)
    membre_habilitats = models.CharField(max_length=255, blank=True)
    membre_carrec_ae_id = models.IntegerField(blank=True, null=True)
    membre_carrec_caec = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ancext_membres'

class AncextMembresNotes(models.Model):
    membres_notes_id = models.IntegerField(primary_key=True)
    membre_id = models.IntegerField()
    nota = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'ancext_membres_notes'

class AncextMembresTipus(models.Model):
    extmem_type_id = models.IntegerField(primary_key=True)
    extmem_type_name = models.CharField(max_length=255)
    extmem_type_description = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'ancext_membres_tipus'

class AncextProjectes(models.Model):
    projecte_id = models.IntegerField(primary_key=True)
    projecte_nom = models.CharField(max_length=255)
    projecte_hashname = models.CharField(max_length=255)
    projecte_descripcio = models.TextField()
    class Meta:
        managed = False
        db_table = 'ancext_projectes'

class AncextProjectesMembres(models.Model):
    projectes_membres_id = models.IntegerField(primary_key=True)
    projecte_id = models.IntegerField()
    membre_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'ancext_projectes_membres'

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
        managed = False
        db_table = 'ref_ciutats'

class RefPaisos(models.Model):
    pai_id = models.IntegerField(primary_key=True)
    pai_cat = models.CharField(max_length=100)
    pai_eng = models.CharField(max_length=100)
    pai_esp = models.CharField(max_length=100)
    pai_extra_int = models.IntegerField()
    pai_extra_text = models.TextField()
    pai_iso3166_1_numeric = models.IntegerField()
    pai_iso3166_1_alfa_2 = models.CharField(max_length=2)
    pai_iso3166_1_alfa_3 = models.CharField(max_length=3)
    pai_gmt = models.FloatField()
    pai_gmt_final = models.FloatField()
    pai_continent = models.IntegerField()
    pai_continent_west_east = models.IntegerField()
    pai_fips = models.CharField(max_length=3)
    pai_capital_cat = models.CharField(max_length=100)
    pai_capital_eng = models.CharField(max_length=100)
    pai_capital_esp = models.CharField(max_length=100)
    pai_km2 = models.IntegerField()
    pai_population = models.IntegerField()
    pai_tld = models.CharField(max_length=3)
    pai_currencycode = models.CharField(max_length=3)
    pai_currencyname = models.CharField(max_length=25)
    pai_phone = models.CharField(max_length=5)
    pai_codpos_format = models.CharField(max_length=25)
    pai_codpos_regex = models.CharField(max_length=25)
    pai_languages = models.CharField(max_length=100)
    pai_geonameid = models.IntegerField()
    pai_neighbours = models.CharField(max_length=100)
    pai_status = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'ref_paisos'

class XarxacatUsers(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'xarxacat_users'