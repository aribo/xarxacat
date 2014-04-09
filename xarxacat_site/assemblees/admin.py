from django.contrib import admin


from cities_light.models import City

from core.actions import export_as_csv_action

from .models import Ae, Carrec_Ae

# Register your models here.


class AeAdmin (admin.ModelAdmin): 
		list_filter = ['constitucio','activitat']
		list_display = ('nom_ca','constitucio','activitat', 'data_constitucio','data_actualitzacio',)
		readonly_fields = ('data_actualitzacio',)
		actions = [export_as_csv_action("CSV Export", fields=['nom_ca', 'nom_en', 'nom', 'email','constitucio','activitat','facebook','twitter','web'])]
		# = ("constitucio",)
#		inlines = [MembreInline,]

class EmailAeAdmin (admin.ModelAdmin):
		list_display = ('ae','email','tipus',)
		
		
admin.site.register(Ae,AeAdmin)
admin.site.register(Carrec_Ae)

