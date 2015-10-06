# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151003_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examenalumno',
            name='nota',
            field=models.IntegerField(null=True, verbose_name=b'Nota'),
        ),
    ]
