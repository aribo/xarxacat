from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xarxacat_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
	url(r'^dashboard/', include('dashboard.urls', namespace ="dashboard")), # dashboard URLS
	url(r'^chaining/', include('smart_selects.urls')), # select chaining URLS (smart-selects)
	
	(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)), # admin URLS
)
