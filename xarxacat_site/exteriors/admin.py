# -*- coding: utf8 -*- 

# imports
from django.contrib import admin

from actions import export_as_csv_action

from exteriors.models import Membre, Ae, Carrec_Ae, Carrec_Caec
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
            'fields': (('dni','data_naixement'),('skype','twitter'),'telefon','poblacio_ext','poblacio_cat',('registre_anc','data_registre_anc'),('numero_anc','sectorial_anc'),('professio','habilitats'),'carrec_ae','carrec_caec','data_actualitzacio')
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
admin.site.register(Carrec_Ae)
admin.site.register(Carrec_Caec)


# Log

from django.contrib import admin
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.utils.html import escape
from django.core.urlresolvers import reverse, NoReverseMatch
from django.contrib.auth.models import User

action_names = {
    ADDITION: 'Addition',
    CHANGE:   'Change',
    DELETION: 'Deletion',
}

class FilterBase(admin.SimpleListFilter):
    def queryset(self, request, queryset):
        if self.value():
            dictionary = dict(((self.parameter_name, self.value()),))
            return queryset.filter(**dictionary)

class ActionFilter(FilterBase):
    title = 'action'
    parameter_name = 'action_flag'
    def lookups(self, request, model_admin):
        return action_names.items()


class UserFilter(FilterBase):
    """Use this filter to only show current users, who appear in the log."""
    title = 'user'
    parameter_name = 'user_id'
    def lookups(self, request, model_admin):
        return tuple((u.id, u.username)
            for u in User.objects.filter(pk__in =
                LogEntry.objects.values_list('user_id').distinct())
        )

class AdminFilter(UserFilter):
    """Use this filter to only show current Superusers."""
    title = 'admin'
    def lookups(self, request, model_admin):
        return tuple((u.id, u.username) for u in User.objects.filter(is_superuser=True))

class StaffFilter(UserFilter):
    """Use this filter to only show current Staff members."""
    title = 'staff'
    def lookups(self, request, model_admin):
        return tuple((u.id, u.username) for u in User.objects.filter(is_staff=True))


class LogEntryAdmin(admin.ModelAdmin):

    date_hierarchy = 'action_time'

    readonly_fields = LogEntry._meta.get_all_field_names()

    list_filter = [
        UserFilter,
        ActionFilter,
        'content_type',
        # 'user',
    ]

    search_fields = [
        'object_repr',
        'change_message'
    ]


    list_display = [
        'action_time',
        'user',
        'content_type',
        'object_link',
        'action_flag',
        'action_description',
        'change_message',
    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser and request.method != 'POST'

    def has_delete_permission(self, request, obj=None):
        return False

    def object_link(self, obj):
        ct = obj.content_type
        repr_ = escape(obj.object_repr)
        try:
            href = reverse('admin:%s_%s_change' % (ct.app_label, ct.model), args=[obj.object_id])
            link = u'<a href="%s">%s</a>' % (href, repr_)
        except NoReverseMatch:
            link = repr_
        return link if obj.action_flag != DELETION else repr_
    object_link.allow_tags = True
    object_link.admin_order_field = 'object_repr'
    object_link.short_description = u'object'

    def queryset(self, request):
        return super(LogEntryAdmin, self).queryset(request) \
            .prefetch_related('content_type')

    def action_description(self, obj):
        return action_names[obj.action_flag]
    action_description.short_description = 'Action'


admin.site.register(LogEntry, LogEntryAdmin)

