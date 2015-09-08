# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150901_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='institucion',
            name='inicio_de_clases',
            field=models.DateField(default=datetime.datetime(2015, 9, 3, 2, 53, 20, 54746, tzinfo=utc), verbose_name=b'Fecha de inicio de clases'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='institucion',
            name='primer_trimestre',
            field=models.DateField(verbose_name=b'Fecha de cierre de notas del primer trimestre'),
        ),
        migrations.AlterField(
            model_name='institucion',
            name='segundo_trimestre',
            field=models.DateField(verbose_name=b'Fecha de cierre de notas del segundo trimestre'),
        ),
        migrations.AlterField(
            model_name='institucion',
            name='tercer_trimestre',
            field=models.DateField(verbose_name=b'Fecha de cierre de notas del tercer trimestre'),
        ),
    ]
