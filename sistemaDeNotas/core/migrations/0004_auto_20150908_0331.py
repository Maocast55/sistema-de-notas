# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150903_0253'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamenAlumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('nota', models.IntegerField(verbose_name=b'Nota')),
                ('alumno', models.ForeignKey(verbose_name=b'Alumno', to='core.Alumno')),
            ],
            options={
                'verbose_name': 'Nota de alumno',
                'verbose_name_plural': 'Nota de alumno',
            },
        ),
        migrations.RemoveField(
            model_name='tipoexamen',
            name='grupo_examen',
        ),
        migrations.RemoveField(
            model_name='examen',
            name='grupo_examen',
        ),
        migrations.DeleteModel(
            name='GrupoExamen',
        ),
        migrations.DeleteModel(
            name='TipoExamen',
        ),
        migrations.AddField(
            model_name='examenalumno',
            name='examen',
            field=models.ForeignKey(verbose_name=b'Examen', to='core.Examen'),
        ),
    ]
