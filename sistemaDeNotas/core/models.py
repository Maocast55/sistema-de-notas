#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class GrupoExamen(models.Model):
    nombre = models.CharField(max_length=64, verbose_name='Nombre')

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Grupo de examen'
        verbose_name_plural = 'Grupos de examen'


class TipoExamen(models.Model):
    codigo = models.CharField(max_length=64, verbose_name='Código')
    descripcion = models.TextField(max_length=128, verbose_name='Descripción')
    nivel = models.PositiveSmallIntegerField(verbose_name='Nivel')
    grupo_examen = models.ForeignKey(GrupoExamen, verbose_name='Grupo examen')

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Tipo de examen"
        verbose_name_plural = "Tipos de examen"


class Seccion(models.Model):
    anio = models.PositiveSmallIntegerField(verbose_name='Año')
    cursada = models.CharField(max_length=64, verbose_name='Cursada')
    grupo = models.CharField(max_length=64, verbose_name='Grupo', null=True, blank=True)

    def __unicode__(self):
        if self.grupo:
            return  self.grupo + self.cursada + ' ' + str(self.anio)
        else:
            return str(self.anio) + self.cursada

    class Meta:
        verbose_name = 'Sección'
        verbose_name_plural = 'Secciones'

class Materia(models.Model):
    nombre = models.CharField(max_length=64, verbose_name='Nombre')
    seccion = models.ForeignKey(Seccion, verbose_name='Sección')
    usuarios = models.ManyToManyField(User, 'Responsable')  # pueden ser docentes, preceptores o administradores.

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'


class Examen(models.Model):
    nombre = models.CharField(max_length=64, verbose_name='Nombre')
    fecha = models.DateField()
    observacion = models.TextField(max_length=512)
    grupo_examen = models.ForeignKey(GrupoExamen, verbose_name='Grupo examen')
    materia = models.ForeignKey(Materia, verbose_name='Materia')

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Examen'
        verbose_name_plural = 'Exámenes'

class Alumno(models.Model):
    primer_nombre = models.CharField(max_length=64, verbose_name='Primer nombre')
    segundo_nombre = models.CharField(max_length=64, verbose_name='Segundo nombre', default='')
    apellido = models.CharField(max_length=64, verbose_name='Apellido')
    dni = models.CharField(max_length=64, verbose_name='dni')

    def __unicode__(self):
        return self.primer_nombre + ' ' + self.segundo_nombre + ' ' + self.apellido

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'

class Inscripcion(models.Model):
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
