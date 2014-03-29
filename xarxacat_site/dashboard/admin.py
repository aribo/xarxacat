from django.contrib import admin

from exteriors.models import Membre
from xarxacat_site.models import XarxacatUsers 
from cities_light.models import City

from smart_selects.db_fields import ChainedForeignKey 

# Register your models here.

admin.site.register(Membre)


