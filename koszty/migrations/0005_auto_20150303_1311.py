# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koszty', '0004_auto_20150303_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='komputer',
            name='MAC',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='komputer',
            name='hostname',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
    ]
