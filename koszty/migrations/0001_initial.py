# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Komputer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('SN', models.CharField(max_length=100)),
                ('MAC', models.CharField(max_length=100, blank=True, null=True)),
                ('hostname', models.CharField(max_length=100, blank=True, null=True)),
                ('standard', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'komputery',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nazwy_Komputer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nazwa', models.CharField(max_length=100)),
                ('koszt', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'nazwy',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usluga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('artikel', models.DecimalField(max_digits=10, decimal_places=0)),
                ('bezeichnung', models.CharField(max_length=250)),
                ('preis', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'uslugi',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='komputer',
            name='nazwa',
            field=models.ForeignKey(to='koszty.Nazwy_Komputer'),
            preserve_default=True,
        ),
    ]
