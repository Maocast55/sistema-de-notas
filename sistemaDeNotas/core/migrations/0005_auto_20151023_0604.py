# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151023_0334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materia',
            name='orden_al_imprimir',
        ),
        migrations.AddField(
            model_name='seccion',
            name='anio_calendario',
            field=models.IntegerField(default=2015),
            preserve_default=False,
        ),
    ]
