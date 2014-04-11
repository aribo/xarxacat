# -*- coding: utf8 -*- 

# imports
from django.contrib import admin
from core.actions import export_as_csv_action
from cities_light.models import City

from .models import Membre
from assemblees.models import Ae


# Register your models here.


class MembreAdmin (admin.ModelAdmin):
		list_filter = ['tipus','carrec_ae', 'carrec_caec','registre_anc','ae','estat']
		list_display = ('full_name','email','tipus', 'ae','Carrec_ae','Carrec_caec', 'pagament','data_actualitzacio',)
		search_fields = ['nom','cognoms','email', 'ae__nom_ca','estat__name']
		readonly_fields = ('data_actualitzacio',)
		actions = [export_as_csv_action("CSV Export", fields=['nom','cognoms','email','ae'])]
		fieldsets = (
        ('Informació bàsica', {
            'fields': (('nom', 'cognoms'), 'email', 'ae', ('tipus','pagament'),('registre_anc','data_registre_anc'),('numero_anc','sectorial_anc'),'activitat', 'data_actualitzacio'), 
        }),
        ('Càrrecs', {
        	'fields': ('carrec_ae','carrec_caec'),
        }),
        ('Localitzacio', {
        	'fields': (('estat', 'codipostal'),'poblacio_ext','poblacio_cat'),
        }),
        ('Personal', {
            'fields': (('dni','data_naixement'),('skype','twitter'),'telefon',('professio','habilitats'))
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
		



# Model registration

admin.site.register(Membre, MembreAdmin)
