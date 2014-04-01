from django.conf.urls import patterns, url

from exteriors import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)