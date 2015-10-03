# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='segundo_nombre',
            field=models.CharField(max_length=64, null=True, verbose_name=b'Segundo nombre', blank=True),
        ),
    ]
