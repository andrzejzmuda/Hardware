from django.db import models
from pracownicy.models import Department, Location
from django.contrib.auth.models import User

class Department2(models.Model):
    department = models.CharField(verbose_name='deptartment2', max_length=100, null=True)
    def __unicode__(self):
        return self.department

class Location2(models.Model):
    location = models.CharField(verbose_name='location2', max_length=100, null=True)
    def __unicode__(self):
        return self.location

class Odpowiedzialny(models.Model):
    odpowiedzialny = models.CharField(verbose_name='odpowiedzialny', max_length=50)
    def __unicode__(self):
        return self.odpowiedzialny

class Tabela_Wnioski(models.Model):
    data_zlozenia_wniosku = models.DateField()
    temat = models.CharField(verbose_name='temat', max_length=400)
    KZZ = models.ForeignKey(User)
    department = models.ForeignKey(Department)
    department2 = models.ForeignKey(Department2)
    location = models.ForeignKey(Location)
    location2 = models.ForeignKey(Location2)
    VV_blitz = models.BooleanField('Blitz Iddee?', default=False)
    oszczednosc = models.DecimalField(max_digits=12, decimal_places=2)
    BHP = models.BooleanField(default=False)
    wprowadzono = models.SmallIntegerField()
    uzasadnienie = models.TextField()
    data_zmiany_statusu = models.DateField()
    odpowiedzialny = models.ForeignKey(Odpowiedzialny)
    zbieranie = models.CharField(max_length=250)
    controlling  = models.CharField(max_length=250)
    punkty = models.SmallIntegerField()
    kwota = models.DecimalField(max_digits=7, decimal_places=2)
    data_wydania_punktow = models.DateField()
    uwagi = models.TextField()
    narada_top_2 = models.DateField()

    class Meta:
        verbose_name_plural = 'Lista_wnioskow'
