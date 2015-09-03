# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='institucion',
            options={'verbose_name': 'Instituci\xf3n', 'verbose_name_plural': 'Instituci\xf3n'},
        ),
        migrations.AddField(
            model_name='institucion',
            name='primer_trimestre',
            field=models.DateField(default=datetime.datetime(2015, 9, 1, 20, 45, 24, 151390, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institucion',
            name='segundo_trimestre',
            field=models.DateField(default=datetime.datetime(2015, 9, 1, 20, 45, 36, 262067, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institucion',
            name='tercer_trimestre',
            field=models.DateField(default=datetime.datetime(2015, 9, 1, 20, 45, 43, 994663, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
