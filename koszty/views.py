from django.shortcuts import render
from koszty.forms import KomputerForm, NazwyForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from koszty.models import Komputer, Nazwy_Komputer, Usluga
from pracownicy.models import Department, Pracownik
from baza.models import Uslugi
from django.db.models import Sum


def dashboard(zadanie):
    dzialy = Department.objects.all()
    return render(zadanie, "koszty/dashboard.html", {'lista': dzialy})

def lista_komputery(zadanie):
    if zadanie.method == 'GET':
        formularz = KomputerForm()
    elif zadanie.method == 'POST':
        formularz = KomputerForm(zadanie.POST)
        if formularz.is_valid():
            Komputer.objects.create(**formularz.cleaned_data)
        return HttpResponseRedirect(reverse('koszty.views.lista_komputery'))
    return render(zadanie, "koszty/lista_komputery.html", {'komputery': Komputer.objects.all(), 'formularz': formularz})


def usun_komputer(zadanie, id):
    skasuj = Komputer.objects.get(pk=id).delete()
    if zadanie.method == 'POST':
        form = KomputerForm(zadanie.POST, instance=skasuj)
        form.u.delete()
        form.save()
    return HttpResponseRedirect(reverse('koszty.views.lista_komputery'))

def edytuj_komputer(zadanie, id):
    zmien = Komputer.objects.get(pk=id)
    nazwy = Nazwy_Komputer.objects.all()
    if zadanie.method == 'POST':
        form = KomputerForm(zadanie.POST, instance=zmien)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('koszty.views.lista_komputery'))
    else:
        form = KomputerForm(instance=zmien)
        return render(zadanie, 'koszty/edytuj_komputer.html', {
            'form': form, 'zmien': zmien, 'nazwy': nazwy
        })

def nazwy_komputery(zadanie):
    if zadanie.method == 'GET':
        formularz = NazwyForm()
    elif zadanie.method == 'POST':
        formularz = NazwyForm(zadanie.POST)
        if formularz.is_valid():
            Nazwy_Komputer.objects.create(**formularz.cleaned_data)
        return  HttpResponseRedirect(reverse('koszty.views.nazwy_komputery'))
    return render(zadanie, "koszty/nazwy_komputery.html", {'nazwy': Nazwy_Komputer.objects.all(), 'formularz': formularz})

def usun_nazwe(zadanie, id):
    skasuj = Nazwy_Komputer.objects.get(pk=id).delete()
    if zadanie.method == 'POST':
        form = NazwyForm(zadanie.POST, instance=skasuj)
        form.u.delete()
        form.save()
    return HttpResponseRedirect(reverse('koszty.views.nazwy_komputery'))

def koszty_dzial(zadanie, id):
    dzial = Department.objects.filter(id=id)
    pracownicy = Pracownik.objects.filter(department_id=dzial)
    pracownicy_dzial = Pracownik.objects.filter(department_id=dzial).values('KZZ').order_by('KZZ')
    uslugi = Uslugi.objects.filter(KZZ=pracownicy_dzial).order_by('KZZ')
    suma = Usluga.objects.filter(uslugi=uslugi).annotate(Sum('preis')).aggregate(Sum('preis'))
    b = ([(e.usluga.bezeichnung) for e in uslugi])
    c = ([float(e.usluga.preis) for e in uslugi])
    calosc = [dzial, pracownicy, uslugi, suma.values()]
    return render(zadanie, "koszty/koszty_dzial.html", {'dzial': dzial, 'pracownicy': pracownicy,
                                                        'uslugi': b, 'suma': suma.values(),
                                                        'cena': c, 'calosc': calosc})

def koszty_pracownik(zadanie, id):
    return render(zadanie, "koszty/koszty_pracownik.html", {'pracownicy': Pracownik.objects.filter(department=id),
                                                            'dzial': Department.objects.filter(id=id)})

def koszty_pracownik_pokaz(zadanie, id):
    pracownik = Pracownik.objects.filter(KZZ=id)
    uslugi = Uslugi.objects.filter(KZZ=id)
    suma = Usluga.objects.filter(uslugi=uslugi).annotate(Sum('preis')).aggregate(Sum('preis'))
    b = ([(e.usluga.bezeichnung) for e in uslugi])
    c = ([float(e.usluga.preis) for e in uslugi])
    return render(zadanie, "koszty/koszty_pracownik_pokaz.html", {'pracownik': pracownik, 'uslugi': b, 'cena': c, 'pracownik_koszt': suma.values()})