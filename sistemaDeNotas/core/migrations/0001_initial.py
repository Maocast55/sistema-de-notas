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
                ('segundo_nombre', models.CharField(max_length=64, null=True, verbose_name=b'Segundo nombre', blank=True)),
                ('apellido', models.CharField(max_length=64, verbose_name=b'Apellido')),
                ('dni', models.CharField(max_length=64, verbose_name=b'dni')),
            ],
            options={
                'verbose_name': 'Alumno',
                'verbose_name_plural': 'Alumnos',
            },
        ),
        migrations.CreateModel(
            name='AlumnoMateriaPromedios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('primero', models.IntegerField()),
                ('segundo', models.IntegerField()),
                ('tercero', models.IntegerField()),
                ('alumno', models.ForeignKey(to='core.Alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=64, verbose_name=b'Nombre')),
                ('fecha', models.DateField()),
                ('observacion', models.TextField(max_length=512, null=True, blank=True)),
                ('trimestre', models.IntegerField()),
                ('es_integrador', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Examen',
                'verbose_name_plural': 'Ex\xe1menes',
            },
        ),
        migrations.CreateModel(
            name='ExamenAlumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('nota', models.IntegerField(null=True, verbose_name=b'Nota')),
                ('alumno', models.ForeignKey(verbose_name=b'Alumno', to='core.Alumno')),
                ('examen', models.ForeignKey(verbose_name=b'Examen', to='core.Examen')),
            ],
            options={
                'verbose_name': 'Nota de alumno',
                'verbose_name_plural': 'Nota de alumno',
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
                ('inicio_de_clases', models.DateField(verbose_name=b'Fecha de inicio de clases')),
                ('primer_trimestre', models.DateField(verbose_name=b'Fecha de cierre de notas del primer trimestre')),
                ('segundo_trimestre', models.DateField(verbose_name=b'Fecha de cierre de notas del segundo trimestre')),
                ('tercer_trimestre', models.DateField(verbose_name=b'Fecha de cierre de notas del tercer trimestre')),
            ],
            options={
                'verbose_name': 'Instituci\xf3n',
                'verbose_name_plural': 'Instituci\xf3n',
            },
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
            name='Preguntas_Administrador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('titulo', models.CharField(max_length=b'255')),
                ('respuesta', models.TextField(max_length=b'4096')),
            ],
            options={
                'verbose_name': 'Pregunta_Administrador',
                'verbose_name_plural': 'Preguntas_Administradores',
            },
        ),
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
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('anio', models.PositiveSmallIntegerField(verbose_name=b'A\xc3\xb1o')),
                ('cursada', models.CharField(max_length=64, verbose_name=b'Cursada')),
                ('grupo', models.CharField(max_length=64, null=True, verbose_name=b'Grupo', blank=True)),
                ('anio_calendario', models.IntegerField(verbose_name=b'A\xc3\xb1o calendario')),
            ],
            options={
                'verbose_name': 'Secci\xf3n',
                'verbose_name_plural': 'Secciones',
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
            name='materia',
            field=models.ForeignKey(verbose_name=b'Materia', to='core.Materia'),
        ),
        migrations.AddField(
            model_name='alumnomateriapromedios',
            name='materia',
            field=models.ForeignKey(to='core.Materia'),
        ),
    ]
