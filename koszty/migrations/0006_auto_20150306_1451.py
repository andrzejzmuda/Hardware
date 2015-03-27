# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koszty', '0005_auto_20150303_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usluga',
            name='preis',
            field=models.DecimalField(max_digits=10, decimal_places=0),
            preserve_default=True,
        ),
    ]
