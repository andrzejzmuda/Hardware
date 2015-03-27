from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^wnioski/$', 'wnioski.views.lista'),
    url(r'^dodaj_wniosek/$', 'wnioski.views.dodaj'),
    url(r'^edytuj_wniosek/(?P<id>\d+)$', 'wnioski.views.edytuj'),
    url(r'^usun_wniosek/(?P<id>\d+)$', 'wnioski.views.usun')

)
