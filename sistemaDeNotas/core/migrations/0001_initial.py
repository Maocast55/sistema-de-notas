# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('primer_nombre', models.CharField(max_length=64, verbose_name=b'Primer nombre')),
                ('segundo_nombre', models.CharField(default=b'', max_length=64, verbose_name=b'Segundo nombre')),
                ('apellido', models.CharField(max_length=64, verbose_name=b'Apellido')),
                ('dni', models.CharField(max_length=64, verbose_name=b'dni')),
            ],
            options={
                'verbose_name': 'Alumno',
                'verbose_name_plural': 'Alumnos',
            },
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=64, verbose_name=b'Nombre')),
                ('fecha', models.DateField()),
                ('observacion', models.TextField(max_length=512)),
            ],
            options={
                'verbose_name': 'Examen',
                'verbose_name_plural': 'Ex\xe1menes',
            },
        ),
        migrations.CreateModel(
            name='GrupoExamen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=64, verbose_name=b'Nombre')),
            ],
            options={
                'verbose_name': 'Grupo de examen',
                'verbose_name_plural': 'Grupos de examen',
            },
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('fecha_alta', models.DateField(verbose_name=b'Fecha alta')),
                ('fecha_hasta', models.DateField(null=True, verbose_name=b'Fecha hasta', blank=True)),
                ('fecha_baja', models.DateField(null=True, verbose_name=b'Fecha baja', blank=True)),
                ('alumno', models.ForeignKey(verbose_name=b'Alumno', to='core.Alumno')),
            ],
            options={
                'verbose_name': 'Inscripci\xf3n',
                'verbose_name_plural': 'Inscripciones',
            },
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=64, verbose_name=b'Nombre de la instituci\xc3\xb3n')),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=64, verbose_name=b'Nombre')),
            ],
            options={
                'verbose_name': 'Materia',
                'verbose_name_plural': 'Materias',
            },
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('anio', models.PositiveSmallIntegerField(verbose_name=b'A\xc3\xb1o')),
                ('cursada', models.CharField(max_length=64, verbose_name=b'Cursada')),
                ('grupo', models.CharField(max_length=64, null=True, verbose_name=b'Grupo', blank=True)),
            ],
            options={
                'verbose_name': 'Secci\xf3n',
                'verbose_name_plural': 'Secciones',
            },
        ),
        migrations.CreateModel(
            name='TipoExamen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=64, verbose_name=b'C\xc3\xb3digo')),
                ('descripcion', models.TextField(max_length=128, verbose_name=b'Descripci\xc3\xb3n')),
                ('nivel', models.PositiveSmallIntegerField(verbose_name=b'Nivel')),
                ('grupo_examen', models.ForeignKey(verbose_name=b'Grupo examen', to='core.GrupoExamen')),
            ],
            options={
                'verbose_name': 'Tipo de examen',
                'verbose_name_plural': 'Tipos de examen',
            },
        ),
        migrations.AddField(
            model_name='materia',
            name='seccion',
            field=models.ForeignKey(verbose_name=b'Secci\xc3\xb3n', to='core.Seccion'),
        ),
        migrations.AddField(
            model_name='materia',
            name='usuarios',
            field=models.ManyToManyField(db_constraint=b'Responsable', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='seccion',
            field=models.ForeignKey(verbose_name=b'Secci\xc3\xb3n', to='core.Seccion'),
        ),
        migrations.AddField(
            model_name='examen',
            name='grupo_examen',
            field=models.ForeignKey(verbose_name=b'Grupo examen', to='core.GrupoExamen'),
        ),
        migrations.AddField(
            model_name='examen',
            name='materia',
            field=models.ForeignKey(verbose_name=b'Materia', to='core.Materia'),
        ),
    ]
