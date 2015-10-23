# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151006_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='orden_al_imprimir',
            field=models.IntegerField(default=1, verbose_name=b'orden al imprimir'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='examen',
            name='observacion',
            field=models.TextField(max_length=512, null=True, blank=True),
        ),
    ]
