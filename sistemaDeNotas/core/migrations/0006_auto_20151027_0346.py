# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20151023_0604'),
    ]

    operations = [
        migrations.AddField(
            model_name='examen',
            name='es_integrador',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='seccion',
            name='anio_calendario',
            field=models.IntegerField(verbose_name=b'A\xc3\xb1o calendario'),
        ),
    ]
