from django.contrib import admin

from .models import Mitja, Agencia, Mitja_Tipus, Agencia_Tipus, Periodista, Periodista_Tipus, Periodista_Carrec

# Register your models here.

class MitjaAdmin(admin.ModelAdmin):
	pass

class Mitja_TipusAdmin(admin.ModelAdmin):
	pass

class AgenciaAdmin(admin.ModelAdmin):
	pass

class Agencia_TipusAdmin(admin.ModelAdmin):
	pass

class PeriodistaAdmin(admin.ModelAdmin):
		list_filter = ['tipus','idioma','mitja', 'agencia','pais']
		list_display = ('full_name','email','tipus', 'pais',)
		def full_name(self,obj):
			return ("%s %s" % (obj.nom, obj.cognoms))
		full_name.short_description = 'Nom'
		actions = [export_as_csv_action("CSV Export", fields=['nom','cognoms','email','pais','idioma'])]

class Periodista_TipusAdmin(admin.ModelAdmin):
	pass

class Periodista_CarrecAdmin(admin.ModelAdmin):
	pass



admin.site.register(Mitja, MitjaAdmin)
admin.site.register(Mitja_Tipus, Mitja_TipusAdmin)
admin.site.register(Agencia, AgenciaAdmin)
admin.site.register(Agencia_Tipus, Agencia_TipusAdmin)
admin.site.register(Periodista, PeriodistaAdmin)
admin.site.register(Periodista_Tipus, Periodista_TipusAdmin)
admin.site.register(Periodista_Carrec, Periodista_CarrecAdmin)

