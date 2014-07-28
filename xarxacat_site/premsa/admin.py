# -*- coding: utf8 -*- 

from django.contrib import admin

from core.actions import export_as_csv_action

from .models import *

# Register your models here.

class MitjaNotaInline(admin.TabularInline):
  model = Mitja_Nota
  extra = 1

class MitjaAdmin(admin.ModelAdmin):
	list_display = ('nom',)
	inlines = ( MitjaNotaInline, )
	ordering = ('nom', )


class Mitja_TipusAdmin(admin.ModelAdmin):
	pass

class AgenciaNotaInline(admin.TabularInline):
	model = Agencia_Nota
	extra = 1

class AgenciaAdmin(admin.ModelAdmin):
	list_display = ('nom',)
	inlines = ( AgenciaNotaInline, )
	ordering = ('nom', )

class Agencia_TipusAdmin(admin.ModelAdmin):
	pass

class PeriodistaNotaInline(admin.TabularInline):
	model = Periodista_Nota
	extra = 1

class PeriodistaAdmin(admin.ModelAdmin):
		list_filter = ['tipus','idioma','mitja', 'agencia','pais', ]
		list_display = ('full_name','email','tipus', 'pais',)
		search_fields = ['full_name','agencia','mitja','email']
		
		fieldsets = (
		('Informació bàsica', { 
			'fields': ('nom','cognoms', 'email','pais_origen', 'idioma') 
			}),
		('Informació professional', {
			'fields': ('tipus','carrec', 'area', 'agencia', 'mitja')
			}),
		('contacte', {
			'fields': ('telefon_fix', 'telefon_mob', 'twitter', 'skype')
			}),
		('localització geogràfica', {
			'fields': ('pais','ciutat','adreca','codipostal')
			}),
		)
		inlines = ( PeriodistaNotaInline, )

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

class Periodista_TipusAdmin(admin.ModelAdmin):
	pass

class Periodista_CarrecAdmin(admin.ModelAdmin):
	pass

class AreaAdmin(admin.ModelAdmin):
	pass


admin.site.register(Area, AreaAdmin)
admin.site.register(Mitja, MitjaAdmin)
admin.site.register(Mitja_Tipus, Mitja_TipusAdmin)
admin.site.register(Agencia, AgenciaAdmin)
admin.site.register(Agencia_Tipus, Agencia_TipusAdmin)
admin.site.register(Periodista, PeriodistaAdmin)
admin.site.register(Periodista_Tipus, Periodista_TipusAdmin)
admin.site.register(Periodista_Carrec, Periodista_CarrecAdmin)

