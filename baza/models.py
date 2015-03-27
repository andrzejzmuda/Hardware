from django.db import models
from django.contrib.auth.models import User
from koszty.models import Komputer, Usluga


class Sprzet(models.Model):
    KZZ = models.ForeignKey(User)
    sprzet = models.ForeignKey(Komputer)
    class Meta:
        verbose_name_plural = 'Lista_sprzetu'
    def __unicode__(self):
        return '%s %s' %(self.KZZ, self.sprzet.hostname)


class Uslugi(models.Model):
    KZZ = models.ForeignKey(User)
    usluga = models.ForeignKey(Usluga, default=0)
    class Meta:
        verbose_name_plural='Lista_uslug'
    def __unicode__(self):
        return '%s %s %d' %(self.KZZ, self.usluga.bezeichnung, self.usluga.preis)
