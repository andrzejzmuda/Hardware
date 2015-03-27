from django.shortcuts import render, render_to_response
from django.template import RequestContext, Context, loader
from baza.models import Sprzet, Uslugi
from koszty.models import Komputer, Usluga
from pracownicy.models import Department, Pracownik
from django.http import HttpResponseRedirect, HttpResponse
import csv
from django.core.urlresolvers import reverse
from baza.forms import SprzetForm, UslugiForm
from django.contrib.auth.models import User

def CSVexport(zadanie):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefile.csv"'
    #writer = csv.writer(response)
    #writer.writerow([Komputer.objects.all()])
    csv_data = Sprzet.objects.all()
    t = loader.get_template('baza/template.txt')
    c = Context({'data': csv_data})
    response.write(t.render(c))
    return response


def Owners(zadanie):
    owners = User.objects.all
    return render_to_response('baza/lista.html',
        {'owners': owners},
        context_instance=RequestContext(zadanie))


def lista(zadanie):
  if zadanie.method == 'GET':
    formularz = SprzetForm()
  elif zadanie.method == 'POST':
    formularz = SprzetForm(zadanie.POST)
    if formularz.is_valid():
      Sprzet.objects.create(**formularz.cleaned_data)
    return HttpResponseRedirect(reverse('baza.views.lista'))
  return render(zadanie, "baza/lista.html", {'Lista_sprzetu': Sprzet.objects.all(), 'formularz': formularz})



def dodaj(zadanie):
    KZZ = User.objects.all()
    sprzet = Komputer.objects.all()
    if zadanie.method == 'GET':
        formularz = SprzetForm()
    elif zadanie.method == 'POST':
        formularz = SprzetForm(zadanie.POST)
        if formularz.is_valid():
          Sprzet.objects.create(**formularz.cleaned_data)
        return HttpResponseRedirect(reverse('baza.views.lista'))
    return render(zadanie, "baza/lista.html", {'Lista_sprzetu': Sprzet.objects.all(), 'KZZ': KZZ, 'sprzet': sprzet, 'formularz': formularz})

def edytuj(zadanie, id):
    zmien = Sprzet.objects.get(pk=id)
    KZZ = User.objects.all()
    sprzet = Komputer.objects.all()
    if zadanie.method == 'POST':
        form = SprzetForm(zadanie.POST, instance=zmien)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('baza.views.lista'))
    else:
        form = SprzetForm(instance=zmien)
        return render(zadanie, 'baza/edytuj.html', {
            'form': form, 'zmien': zmien, 'KZZ': KZZ, 'sprzet': sprzet
        })


def usun(zadanie, id):
    skasuj = Sprzet.objects.get(pk=id).delete()
    if zadanie.method == 'POST':
        form = SprzetForm(zadanie.POST, instance=skasuj)
        form.u.delete()
        form.save()
    return HttpResponseRedirect('/lista/')


def uslugi(zadanie):
  if zadanie.method == 'GET':
    formularz = UslugiForm()
  elif zadanie.method == 'POST':
    formularz = UslugiForm(zadanie.POST)
    if formularz.is_valid():
      Uslugi.objects.create(**formularz.cleaned_data)
    return HttpResponseRedirect(reverse('baza.views.uslugi'))
  return render(zadanie, "baza/uslugi.html", {'Lista_uslug': Uslugi.objects.all(), 'formularz': formularz})


def dodaj_usluge(zadanie):
    KZZ = User.objects.all()
    usluga = Usluga.objects.all()
    if zadanie.method == 'GET':
        formularz = UslugiForm()
    elif zadanie.method == 'POST':
        formularz = UslugiForm(zadanie.POST)
        if formularz.is_valid():
          Uslugi.objects.create(**formularz.cleaned_data)
        return HttpResponseRedirect(reverse('baza.views.uslugi'))
    return render(zadanie, "baza/dodaj_usluge.html", {'KZZ': KZZ, 'usluga': usluga, 'formularz': formularz})

def usun_usluge(zadanie, id):
    skasuj = Uslugi.objects.get(pk=id).delete()
    if zadanie.method == 'POST':
        form = UslugiForm(zadanie.POST, instance=skasuj)
        form.u.delete()
        form.save()
    return HttpResponseRedirect('/uslugi/')

def edytuj_usluge(zadanie, id):
    zmien = Uslugi.objects.get(pk=id)
    KZZ = User.objects.all()
    if zadanie.method == 'POST':
        form = UslugiForm(zadanie.POST, instance=zmien)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('baza.views.uslugi'))
    else:
        form = UslugiForm(instance=zmien)
        return render(zadanie, 'baza/edytuj_usluge.html', {
            'form': form, 'usluga': zmien, 'KZZ': KZZ
        })