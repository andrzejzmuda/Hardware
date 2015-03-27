from django.conf.urls import patterns, include, url


urlpatterns = patterns('koszty',

    url(r'^dashboard', 'views.dashboard'),
    url(r'^lista_komputery/$', 'views.lista_komputery'),
    url(r'^edytuj_komputer/(?P<id>\d+)$', 'views.edytuj_komputer'),
    url(r'^usun_komputer/(?P<id>\d+)$', 'views.usun_komputer'),
    url(r'^nazwy_komputery/$', 'views.nazwy_komputery'),
    url(r'^usun_nazwe/(?P<id>\d+)$', 'views.usun_nazwe'),
    url(r'^koszty_dzial/(?P<id>\d+)$', 'views.koszty_dzial'),
    url(r'^koszty_pracownik/(?P<id>\d+)$', 'views.koszty_pracownik'),
    url(r'^koszty_pracownik_pokaz/(?P<id>\d+)$', 'views.koszty_pracownik_pokaz'),

)
