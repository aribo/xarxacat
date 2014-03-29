from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xarxacat_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
	url(r'^dashboard/', include('dashboard.urls', namespace ="dashboard")),
	url(r'^chaining/', include('smart_selects.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
