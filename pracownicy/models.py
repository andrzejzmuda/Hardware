from django.db import models
from django.contrib.auth.models import User



class Department(models.Model):
    department = models.CharField(verbose_name='dept', max_length=100, null=False)
    def __unicode__(self):
        return self.department

class Location(models.Model):
    location = models.CharField(verbose_name='location', max_length=100, null=False)
    def __unicode__(self):
        return self.location

class Werk(models.Model):
    werk = models.CharField(verbose_name='werk', max_length=100, null=False)
    def __unicode__(self):
        return self.werk


class Pracownik(models.Model):
    KZZ = models.OneToOneField(User)
    imie = models.CharField(max_length=150, verbose_name='imie', null=False)
    nazwisko = models.CharField(max_length=150, verbose_name='nazwisko', null=False)
    department = models.ForeignKey(Department)
    location = models.ForeignKey(Location)
    werk = models.ForeignKey(Werk)
    MPK = models.CharField(max_length=20, verbose_name='MPK', null=True)

    def __unicode__(self):
        return '%s' %(self.KZZ)
    class Meta:
        verbose_name_plural='Pracownicy'
