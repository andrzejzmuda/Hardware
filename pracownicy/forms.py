from django import forms
from django.contrib.auth.models import User
from pracownicy.models import Department, Location, Werk, Pracownik
import autocomplete_light
autocomplete_light.autodiscover()

class PracownicyForm(forms.ModelForm):
    class Meta:
        model = Pracownik

class WerkForm(forms.ModelForm):
    class Meta:
        model = Werk

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location