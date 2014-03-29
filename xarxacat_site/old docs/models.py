# Models of cities and countries of old system

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

class Ciutat(models.Model):
    name = models.CharField(max_length=100) 
    countrycode = models.CharField(max_length=3)
    pais = models.ForeignKey(Pais)
    nada = models.IntegerField()
    district = models.CharField(max_length=20)
    population = models.IntegerField()
    lat = models.FloatField()
    longi = models.FloatField()
    provincia = models.IntegerField()
    comarca = models.IntegerField()
    sinonims = models.CharField(max_length=100)
    cat = models.CharField(max_length=100)
    def __unicode__(self): 
    	return self.name
    class Meta:
        ordering = ['name']
