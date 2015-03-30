from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Hardware.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),__author__ = 'andrzej'
    url(r'^$', 'baza.views.lista'),
    url(r'^lista/$', 'baza.views.lista'),
    url(r'^sprzet/(?P<id>\d+)$', 'baza.views.dodaj'),
    url(r'^edytuj/(?P<id>\d+)$', 'baza.views.edytuj'),
    url(r'^dodaj/$', 'baza.views.dodaj'),
    url(r'^usun/(?P<id>\d+)$', 'baza.views.usun'),
    url(r'^pracownicy/$', 'pracownicy.views.lista'),
    url(r'^dashboard/$', 'koszty.views.dashboard'),
    url(r'^uslugi/$', 'baza.views.uslugi'),
    url(r'^dodaj_usluge/$', 'baza.views.dodaj_usluge'),
    url(r'^usun_usluge/(?P<id>\d+)$', 'baza.views.usun_usluge'),
    url(r'^edytuj_usluge/(?P<id>\d+)$', 'baza.views.edytuj_usluge'),
    url(r'^CSVexport/$', 'baza.views.CSVexport')


)
