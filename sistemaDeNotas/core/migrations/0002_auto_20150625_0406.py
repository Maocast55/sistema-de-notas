# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripcion',
            name='fecha_baja',
            field=models.DateField(null=True, verbose_name=b'Fecha baja'),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='fecha_hasta',
            field=models.DateField(null=True, verbose_name=b'Fecha hasta'),
        ),
        migrations.AlterField(
            model_name='seccion',
            name='grupo',
            field=models.CharField(max_length=64, null=True, verbose_name=b'Grupo'),
        ),
    ]
