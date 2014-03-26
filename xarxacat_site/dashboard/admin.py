from django.contrib import admin

from dashboard.models import Pais
from exteriors.models import Membre
from xarxacat_site.models import XarxacatUsers 

# Register your models here.

admin.site.register(Membre)
admin.site.register(Pais)
