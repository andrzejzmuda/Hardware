from django.db import models

class Nazwy_Komputer(models.Model):
    nazwa = models.CharField(max_length=100)
    koszt = models.FloatField()
    def __unicode__(self):
        return '%s' %(self.nazwa)
    class Meta:
        verbose_name_plural = 'nazwy'

class Komputer(models.Model):
    nazwa = models.ForeignKey(Nazwy_Komputer)
    SN = models.CharField(max_length=100)
    MAC = models.CharField(max_length=100, null=True)
    hostname = models.CharField(max_length=100, null=True)
    standard = models.BooleanField(default=True)
    def __unicode__(self):
        return '%s %s' %(self.hostname, self.nazwa)
    class Meta:
        verbose_name_plural = 'komputery'

class Usluga(models.Model):
    artikel = models.DecimalField(decimal_places=0, max_digits=10)
    bezeichnung = models.CharField(max_length=250)
    preis = models.DecimalField(decimal_places=0, max_digits=10)
    def __unicode__(self):
        return '%s %s %s' %(self.artikel, self.bezeichnung, self.preis)
    class Meta:
        verbose_name_plural = 'uslugi'