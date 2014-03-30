# -*- coding: utf8 -*- 

# imports
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
		list_filter = ['tipus','carrec_ae', 'carrec_caec','registre_anc','ae','estat']
		list_display = ('full_name','email','tipus', 'ae','Carrec_ae','Carrec_caec', 'pagament','data_actualitzacio',)
		search_fields = ['nom','cognoms','email', 'ae__nom_ca','estat__name_ascii']
		readonly_fields = ('data_actualitzacio',)
		actions = [export_as_csv_action("CSV Export", fields=['nom','cognoms','email','ae'])]
		fieldsets = (
        ('Informació bàsica', {
            'fields': (('nom', 'cognoms'), 'email', 'ae', ('estat', 'codipostal'), ('tipus','pagament'))
        }),
        ('Dades extras', {
            'classes': ('collapse',),
            'fields': (('dni','data_naixement'),('skype','telefon'),'poblacio_ext','poblacio_cat',('registre_anc','data_registre_anc'),('numero_anc','sectorial_anc'),('professio','habilitats'),'carrec_ae','carrec_caec','data_actualitzacio')
        }),
		)
		
		def full_name(self,obj):
			return ("%s %s" % (obj.nom, obj.cognoms))
		full_name.short_description = 'Nom'
		
		def formfield_for_foreignkey(self, db_field, request, **kwargs):
			if db_field.name == "ae":
				kwargs["queryset"] = Ae.objects.order_by('-constitucio','nom_ca')
			return super(MembreAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
		
		def Carrec_ae(self, obj):
			carrecs_ae = [p.nom for p in obj.carrec_ae.all()]
			ae = ", ".join(carrecs_ae)
			return ae
		Carrec_ae.short_description = 'Carrec/s AE'
		
		def Carrec_caec(self, obj):
			carrecs_caec = [p.nom for p in obj.carrec_caec.all()]
			caec = ", ".join(carrecs_caec)
			return caec
		Carrec_caec.short_description = 'Carrec/s CAEC'
			
		
		

class AeAdmin (admin.ModelAdmin): 
		list_filter = ['constitucio','activitat']
		list_display = ('nom_ca','constitucio','activitat', 'data_constitucio','data_actualitzacio',)
		readonly_fields = ('data_actualitzacio',)
		actions = [export_as_csv_action("CSV Export", fields=['nom','email','constitucio','activitat','facebook','twitter','web'])]
		# = ("constitucio",)
#		inlines = [MembreInline,]


admin.site.register(Membre, MembreAdmin)
admin.site.register(Ae,AeAdmin)




