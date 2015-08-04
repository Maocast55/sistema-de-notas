# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150625_0406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscripcion',
            name='anio_lectivo',
        ),
    ]
