from django import forms
from wnioski.models import Tabela_Wnioski, Odpowiedzialny, Department2, Location2
from pracownicy.models import Department, Location
from django.contrib.auth.models import User

class WnioskiForm(forms.ModelForm):
    class Meta:
        model = Tabela_Wnioski
        KZZ = forms.ModelChoiceField(queryset=User.objects.all())
        department = forms.ModelChoiceField(queryset=Department.objects.all())
        department2 = forms.ModelChoiceField(queryset=Department2.objects.all())
        location = forms.ModelChoiceField(queryset=Location.objects.all())
        location2 = forms.ModelChoiceField(queryset=Location2.objects.all())
        odpowiedzialny = forms.ModelChoiceField(queryset=Odpowiedzialny.objects.all())
    '''
    class Meta:
        set(Tabela_Wnioski.__add__)
'''