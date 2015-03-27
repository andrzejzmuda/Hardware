from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', 'pracownicy.views.lista'),
    url(r'^pracownicy/$', 'pracownicy.views.lista'),
    url(r'^sprzet/$', 'baza.views.lista'),
    url(r'^dodaj_pracownika/$', 'pracownicy.views.dodaj'),
    url(r'^edytuj_pracownika/(?P<id>\d+)$', 'pracownicy.views.edytuj'),
    url(r'^usun_pracownika/(?P<id>\d+)$', 'pracownicy.views.usun'),
    url(r'^sprzet_uzytkownika/(?P<id>\d+)$', 'pracownicy.views.sprzet_uzytkownika'),
    url(r'^dodaj_werk/$', 'pracownicy.views.dodaj_werk'),
    url(r'^usun_werk/(?P<id>\d+)$', 'pracownicy.views.usun_werk'),
    url(r'^dodaj_dzial/$', 'pracownicy.views.dodaj_dzial'),
    url(r'^usun_dzial/(?P<id>\d+)$', 'pracownicy.views.usun_dzial'),
    url(r'^dodaj_lokalizacje/$', 'pracownicy.views.dodaj_lokalizacje'),
    url(r'^usun_lokalizacje/(?P<id>\d+)$', 'pracownicy.views.usun_lokalizacje'),

)
