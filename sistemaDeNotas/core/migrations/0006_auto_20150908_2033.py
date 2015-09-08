# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_pregunta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preguntas_Frecuentes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('titulo', models.CharField(max_length=b'255')),
                ('respuesta', models.TextField(max_length=b'4096')),
            ],
            options={
                'verbose_name': 'Pregunta_Frecuente',
                'verbose_name_plural': 'Preguntas_Frecuentes',
            },
        ),
        migrations.CreateModel(
            name='Preguntas_Profesor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('titulo', models.CharField(max_length=b'255')),
                ('respuesta', models.TextField(max_length=b'4096')),
            ],
            options={
                'verbose_name': 'Pregunta_Profesor',
                'verbose_name_plural': 'Preguntas_Profesores',
            },
        ),
        migrations.RenameModel(
            old_name='Pregunta',
            new_name='Preguntas_Administrador',
        ),
        migrations.AlterModelOptions(
            name='preguntas_administrador',
            options={'verbose_name': 'Pregunta_Administrador', 'verbose_name_plural': 'Preguntas_Administradores'},
        ),
    ]
