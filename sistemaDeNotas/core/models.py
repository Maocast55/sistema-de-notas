#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Seccion(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    anio = models.PositiveSmallIntegerField(verbose_name='Año')
    cursada = models.CharField(max_length=64, verbose_name='Cursada')
    grupo = models.CharField(max_length=64, verbose_name='Grupo', null=True, blank=True)

    def __unicode__(self):
        if self.grupo:
            return  self.cursada + self.grupo + ' ' + str(self.anio)
        else:
            return self.cursada + str(self.anio)

    class Meta:
        verbose_name = 'Sección'
        verbose_name_plural = 'Secciones'

class Materia(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    nombre = models.CharField(max_length=64, verbose_name='Nombre')
    seccion = models.ForeignKey(Seccion, verbose_name='Sección')
    usuarios = models.ManyToManyField(User, 'Responsable')  # pueden ser docentes, preceptores o administradores.

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'


class Examen(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    nombre = models.CharField(max_length=64, verbose_name='Nombre')
    fecha = models.DateField()
    observacion = models.TextField(max_length=512)
    materia = models.ForeignKey(Materia, verbose_name='Materia')

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Examen'
        verbose_name_plural = 'Exámenes'

class Alumno(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    primer_nombre = models.CharField(max_length=64, verbose_name='Primer nombre')
    segundo_nombre = models.CharField(max_length=64, verbose_name='Segundo nombre', default='')
    apellido = models.CharField(max_length=64, verbose_name='Apellido')
    dni = models.CharField(max_length=64, verbose_name='dni')

    def __unicode__(self):
        return self.primer_nombre + ' ' + self.segundo_nombre + ' ' + self.apellido

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'

class ExamenAlumno(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    alumno = models.ForeignKey(Alumno, verbose_name='Alumno')
    examen = models.ForeignKey(Examen, verbose_name='Examen')
    nota = models.IntegerField(verbose_name='Nota')

    def __unicode__(self):
        return self.alumno + '|' + self.examen + '|' + self.nota

    class Meta:
        verbose_name = 'Nota de alumno'
        verbose_name_plural = 'Nota de alumno'


class Inscripcion(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    fecha_alta = models.DateField(verbose_name='Fecha alta')        # fecha en la que se inicia la inscripción
    fecha_hasta = models.DateField(verbose_name='Fecha hasta', null=True, blank=True)      # el alumno se cambió de sección o finalizó el ciclo lectivo
    fecha_baja = models.DateField(verbose_name='Fecha baja', null=True, blank=True)        # el alumno se fue del colegio
    seccion = models.ForeignKey(Seccion, verbose_name='Sección')
    alumno = models.ForeignKey(Alumno, verbose_name='Alumno')

    def __unicode__(self):
        return str(self.seccion) + ' | ' + str(self.alumno)


    class Meta:
        verbose_name = 'Inscripción'
        verbose_name_plural = 'Inscripciones'

class Institucion(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    nombre = models.CharField(max_length=64, verbose_name='Nombre de la institución')

    # Fechas de finalización de los trimestres en esa institución
    inicio_de_clases = models.DateField(verbose_name='Fecha de inicio de clases')
    primer_trimestre = models.DateField(verbose_name='Fecha de cierre de notas del primer trimestre')
    segundo_trimestre = models.DateField(verbose_name='Fecha de cierre de notas del segundo trimestre')
    tercer_trimestre = models.DateField(verbose_name='Fecha de cierre de notas del tercer trimestre')

    def __unicode__(self):
        return self.nombre


    class Meta:
        verbose_name = 'Institución'
        verbose_name_plural = 'Institución'