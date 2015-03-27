from django.shortcuts import render
from pracownicy.forms import PracownicyForm, WerkForm, DepartmentForm, LocationForm
from pracownicy.models import Pracownik, Department, Location, Werk
from baza.models import Sprzet, Uslugi
from koszty.models import Usluga
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def lista(zadanie):
    if zadanie.method == 'GET':
        formularz = PracownicyForm()
    elif zadanie.method == 'POST':
        formularz = PracownicyForm(zadanie.POST)
        if formularz.is_valid():
          Pracownik.objects.create(**formularz.cleaned_data)
        return HttpResponseRedirect(reverse('pracownicy.views.lista'))
    return render(zadanie, "pracownicy/lista.html", {'Pracownicy': Pracownik.objects.all(), 'formularz': formularz})


def dodaj(zadanie):
    KZZ = User.objects.all()
    department = Department.objects.all()
    location = Location.objects.all()
    werk = Werk.objects.all()
    if zadanie.method == 'GET':
        formularz = PracownicyForm()
    elif zadanie.method == 'POST':
        formularz = PracownicyForm(zadanie.POST)
        if formularz.is_valid():
          Pracownik.objects.create(**formularz.cleaned_data)
        return HttpResponseRedirect(reverse('pracownicy.views.lista'))
    return render(zadanie, "pracownicy/dodaj.html", {'Pracownicy': Pracownik.objects.all(), 'KZZ': KZZ, 'department': department,
                                               'location': location, 'werk': werk, 'formularz': formularz})

def edytuj(zadanie, id):
    zmien = Pracownik.objects.get(pk=id)
    KZZ = User.objects.all()
    location = Location.objects.all()
    werk = Werk.objects.all()
    department = Department.objects.all()
    if zadanie.method == 'POST':
        form = PracownicyForm(zadanie.POST, instance=zmien)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pracownicy.views.lista'))
    else:
        form = PracownicyForm(instance=zmien)

        return render(zadanie, 'pracownicy/edytuj.html', {
            'form': form, 'pracownik': zmien, 'KZZ': KZZ, 'location': location,
            'werk': werk, 'department': department
        })


def usun(zadanie, id):
    skasuj = Pracownik.objects.get(pk=id).delete()
    if zadanie.method == 'POST':
        form = PracownicyForm(zadanie.POST, instance=skasuj)
        form.u.delete()
        form.save()
    return HttpResponseRedirect(reverse('pracownicy.views.lista'))


def sprzet_uzytkownika(zadanie, id):
    sprzet_uzytkownika = Sprzet.objects.filter(KZZ_id=id)
    uzytkownik = Pracownik.objects.filter(KZZ=id)
    return render(zadanie, 'pracownicy/pokaz.html', {'sprzet_uzytkownika': sprzet_uzytkownika, 'uzytkownik': uzytkownik})

def dodaj_werk(zadanie):
    werk = Werk.objects.all()
    if zadanie.method == 'GET':
        formularz = WerkForm()
    elif zadanie.method == 'POST':
        formularz = WerkForm(zadanie.POST)
        if formularz.is_valid():
          Werk.objects.create(**formularz.cleaned_data)
        return HttpResponseRedirect(reverse('pracownicy.views.dodaj_werk'))
    return render(zadanie, "pracownicy/dodaj_werk.html", {'werk': werk, 'formularz': formularz})

def usun_werk(zadanie, id):
    skasuj = Werk.objects.get(pk=id).delete()
    if zadanie.method == 'POST':
        form = WerkForm(zadanie.POST, instance=skasuj)
        form.u.delete()
        form.save()
    return HttpResponseRedirect(reverse('pracownicy.views.dodaj_werk'))

def dodaj_dzial(zadanie):
    department = Department.objects.all()
    if zadanie.method == 'GET':
        formularz = DepartmentForm()
    elif zadanie.method == 'POST':
        formularz = DepartmentForm(zadanie.POST)
        if formularz.is_valid():
            Department.objects.create(**formularz.cleaned_data)
        return HttpResponseRedirect(reverse('pracownicy.views.dodaj_dzial'))
    return render(zadanie, "pracownicy/dodaj_dzial.html", {'department': department, 'formularz': formularz})

def usun_dzial(zadanie, id):
    skasuj = Department.objects.get(pk=id).delete()
    if zadanie.method == 'POST':
        form = DepartmentForm(zadanie.POST, instance=skasuj)
        form.u.delete()
        form.save()
    return HttpResponseRedirect(reverse('pracownicy.views.dodaj_dzial'))

def dodaj_lokalizacje(zadanie):
    lokalizacja = Location.objects.all()
    if zadanie.method == 'GET':
        formularz = LocationForm()
    elif zadanie.method == 'POST':
        formularz = LocationForm(zadanie.POST)
        if formularz.is_valid():
          Location.objects.create(**formularz.cleaned_data)
        return HttpResponseRedirect(reverse('pracownicy.views.dodaj_lokalizacje'))
    return render(zadanie, "pracownicy/dodaj_lokalizacje.html", {'location': lokalizacja, 'formularz': formularz})

def usun_lokalizacje(zadanie, id):
    skasuj = Location.objects.get(pk=id).delete()
    if zadanie.method == 'POST':
        form = LocationForm(zadanie.POST, instance=skasuj)
        form.u.delete()
        form.save()
    return HttpResponseRedirect(reverse('pracownicy.views.dodaj_lokalizacje'))