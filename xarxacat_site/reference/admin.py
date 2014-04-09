from django.contrib import admin

from reference.models import Idioma, PaisIdioma

# Register your models here.

class PaisIdiomaAdmin (admin.ModelAdmin):
		filter_horizontal = ('idioma',)

admin.site.register(Idioma)
admin.site.register(PaisIdioma, PaisIdiomaAdmin)
