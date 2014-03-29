from django.contrib import admin

from actions import export_as_csv_action

from exteriors.models import Membre, Ae
from xarxacat_site.models import XarxacatUsers 
from cities_light.models import City
 
 
# functions

 

# Register your models here.

#class MembreInline(admin.TabularInline):
#    	model = Membre
#    	extra = 5
#    	fields = ('nom','cognoms','email')

class MembreAdmin (admin.ModelAdmin):
		list_filter = ['tipus','registre_anc','ae','estat']
		list_display = ('full_name','ae','tipus','pagament','data_actualitzacio',)
		search_fields = ['nom','cognoms','ae__nom_ca',]
		readonly_fields = ('data_actualitzacio',)
		actions = [export_as_csv_action("CSV Export", fields=['nom','cognoms','email','ae'])]
		
		def full_name(self,obj):
			return ("%s %s" % (obj.nom, obj.cognoms))
		full_name.short_description = 'Nom'
		
		

class AeAdmin (admin.ModelAdmin): 
		list_filter = ['constitucio','activitat']
		list_display = ('nom_ca','constitucio','activitat', 'data_constitucio','data_actualitzacio','num_members')
		readonly_fields = ('data_actualitzacio',)
		actions = [export_as_csv_action("CSV Export", fields=['nom','email','constitucio','activitat','facebook','twitter','web'])]
		# = ("constitucio",)
#		inlines = [MembreInline,]

		def num_members(self,obj):
			return ("%s" % (obj.nom))
		num_members.short_description = "Num"


admin.site.register(Membre, MembreAdmin)
admin.site.register(Ae,AeAdmin)




