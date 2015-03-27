from django import forms
from koszty.models import Komputer, Nazwy_Komputer
from baza.models import Uslugi

class KomputerForm(forms.ModelForm):
    class Meta:
        model = Komputer


class NazwyForm(forms.ModelForm):
    class Meta:
        model = Nazwy_Komputer



