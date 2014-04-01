from django.conf.urls import patterns, url

from tauler import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)