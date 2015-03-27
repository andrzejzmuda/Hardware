from django.shortcuts import render
from wnioski.forms import WnioskiForm
from wnioski.models import Tabela_Wnioski, Odpowiedzialny, Location2, Department2
from pracownicy.models import Department, Location
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


def lista(zadanie):
    if zadanie.method == 'GET':
        formularz = WnioskiForm()
    elif zadanie.method == 'POST':
        formularz = WnioskiForm(zadanie.POST)
        if formularz.is_valid():
          Tabela_Wnioski.objects.create(**formularz.cleaned_data)
        return HttpResponseRedirect(reverse('wnioski.views.lista'))
    return render(zadanie, "wnioski/lista.html", {'Lista_Wnioskow': Tabela_Wnioski.objects.all(), 'formularz': formularz})


def dodaj(zadanie):
    KZZ = User.objects.all()
    department = Department.objects.all()
    department2 = Department2.objects.all()
    location = Location.objects.all()
    location2 = Location2.objects.all()
    odpowiedzialny = Odpowiedzialny.objects.all()
    if zadanie.method == 'GET':
        formularz = WnioskiForm()
    elif zadanie.method == 'POST':
        formularz = WnioskiForm(zadanie.POST)
        if formularz.is_valid():
          Tabela_Wnioski.objects.create(**formularz.cleaned_data)
        return HttpResponseRedirect(reverse('wnioski.views.lista'))
    return render(zadanie, "wnioski/dodaj.html", {'Wnioski': Tabela_Wnioski.objects.all(), 'KZZ': KZZ, 'department': department, 'department2': department2,
                                               'location': location, 'location2': location2, 'odpowiedzialny' : odpowiedzialny, 'formularz': formularz})


def edytuj(zadanie, id):
    zmien = Tabela_Wnioski.objects.get(pk=id)
    KZZ = User.objects.all()
    location = Location.objects.all()
    location2 = Location2.objects.all()
    department = Department.objects.all()
    department2 = Department2.objects.all()
    odpowiedzialny = Odpowiedzialny.objects.all()
    if zadanie.method == 'POST':
        form = WnioskiForm(zadanie.POST, instance=zmien)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('wnioski.views.lista'))
    else:
        form = WnioskiForm(instance=zmien)

        return render(zadanie, 'wnioski/edytuj.html', {
            'form': form, 'wniosek': zmien, 'KZZ': KZZ, 'location': location,
            'location2': location2, 'department': department, 'department2': department2, 'odpowiedzialny': odpowiedzialny
        })

def usun(zadanie, id):
    skasuj = Tabela_Wnioski.objects.get(pk=id).delete()
    if zadanie.method == 'POST':
        form = Tabela_Wnioski(zadanie.POST, instance=skasuj)
        form.u.delete()
        form.save()
    return HttpResponseRedirect(reverse('wnioski.views.lista'))

def stopien_realizacji_wnioskow(zadanie):
    realizacja_kable = Tabela_Wnioski.objects.filter(department_id=13)