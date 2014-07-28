# -*- coding: utf8 -*- 

from django.contrib import admin

from core.actions import export_as_csv_action

from .models import *

# Register your models here.

class AreaAdmin(admin.ModelAdmin):
	pass


class OrganitzacioNotaInline(admin.TabularInline):
	model = Organitzacio_Nota
	extra = 1

class OrganitzacioAdmin(admin.ModelAdmin):
	list_display = ('nom',)
	inlines = ( OrganitzacioNotaInline, )
	ordering = ('nom', )
	

	
class Organitzacio_TipusAdmin(admin.ModelAdmin):
	pass
	

class PersonalitatNotaInline(admin.TabularInline):
	model = Personalitat_Nota
	extra = 1

class PersonalitatAdmin(admin.ModelAdmin):
		list_filter = ['area','idioma','organitzacio', 'pais', ]
		list_display = ('full_name','email','area', 'pais',)
		search_fields = ['full_name','organitzacio', 'email']
		
		fieldsets = (
		('Informació bàsica', { 
			'fields': ('nom','cognoms', 'email','pais_origen', 'idioma') 
			}),
		('Informació professional', {
			'fields': ('carrec', 'area', 'organitzacio')
			}),
		('contacte', {
			'fields': ('telefon_fix', 'telefon_mob', 'twitter', 'skype')
			}),
		('localització geogràfica', {
			'fields': ('pais','ciutat','adreca','codipostal')
			}),
		)
		
		inlines = ( PersonalitatNotaInline, )

		''' to display the first name of the user as created by http://stackoverflow.com/questions/163823/can-list-display-in-a-django-modeladmin-display-attributes-of-foreignkey-field
		def createdby_firstname(self, obj):
			return obj.created_by.first_name
		createdby_firstname.short_description = 'Creat per'
		'''
		
		def full_name(self,obj):
			return ("%s %s" % (obj.nom, obj.cognoms))
		full_name.short_description = 'Nom'
		actions = [export_as_csv_action("CSV Export", fields=['nom','cognoms','email','pais','idioma'])]
		
		def save_model(self, request, obj, form, change):
			if getattr(obj, 'created_by', None) is None:
				obj.created_by = request.user
			obj.save()




admin.site.register(Area, AreaAdmin)
admin.site.register(Organitzacio, OrganitzacioAdmin)
admin.site.register(Organitzacio_Tipus, Organitzacio_TipusAdmin)
admin.site.register(Personalitat, PersonalitatAdmin)