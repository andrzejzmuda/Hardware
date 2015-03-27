from django import forms
from django.contrib.auth.models import User
from baza.models import Sprzet, Uslugi
from koszty.models import Komputer, Usluga
import autocomplete_light
autocomplete_light.autodiscover()

class SprzetForm(forms.ModelForm):
    class Meta:
        model = Sprzet
        KZZ = forms.ModelChoiceField(queryset=User.objects.all().values())
        Komputer = forms.ModelChoiceField(queryset=Sprzet.objects.all().values())

class UslugiForm(forms.ModelForm):
    class Meta:
        model = Uslugi
        KZZ = forms.ModelChoiceField(queryset=User.objects.all())
        Usluga = forms.ModelChoiceField(queryset=Usluga.objects.all())

