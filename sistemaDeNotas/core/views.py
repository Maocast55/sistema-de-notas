#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from core.forms import LoginForm, ChangePasswordForm
from core.models import User, Institucion, Materia, Preguntas_Administrador, Preguntas_Profesor, Preguntas_Frecuentes
from django.contrib.auth import login, authenticate, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from datetime import date

# Filtros para usar en los templates
from django.template.defaulttags import register


@register.filter
def get_estado_de_trimestre(materia, args):
    '''
    :param materia: Una materia
    :param args: 'Clave' ==> puede ser '1' (si se quieren obtener el estado de un trimestre)
    o '2' (si se quiere obtener si el botón debe estar habilitado)
    'Trimestre' ==> Puede ser 1,2 o 3.
    :return: Diccionario (en '1' están los estados de los trimestres. En '2' dice si que botones se habilitan de accesos)
    '''
    arg_list = [arg.strip() for arg in args.split(',')]
    trimestre = arg_list[0]
    clave = arg_list[1]

    institucion = Institucion.objects.all()[0]

    # Estados de los trimestres = Clase bootstrap que va a mostrarse
    estado_primer_trimestre = None
    estado_segundo_trimestre = None
    estado_tercer_trimestre = None

    # Habilitado trimestre = Booleano que indica si tiene que estar habilitada la visibilidad de la materia
    habilitao_primer_trimestre = None
    habilitado_segundo_trimestre = None
    habilitado_tercer_trimestre = None

    if institucion.inicio_de_clases > date.today():
        # Aún no iniciaron las clases
        estado_primer_trimestre = 'fa fa-clock-o'
        estado_segundo_trimestre = 'fa fa-clock-o'
        estado_tercer_trimestre = 'fa fa-clock-o'
        habilitao_primer_trimestre = False
        habilitado_segundo_trimestre = False
        habilitado_tercer_trimestre = False

    elif institucion.inicio_de_clases < date.today() and date.today() < institucion.primer_trimestre:
        # El primer trimestre está en curso
        estado_primer_trimestre = calcular_estado_de_materia(materia, trimestre)
        estado_segundo_trimestre = 'fa fa-clock-o'
        estado_tercer_trimestre = 'fa fa-clock-o'
        habilitao_primer_trimestre = True
        habilitado_segundo_trimestre = False
        habilitado_tercer_trimestre = False

    elif institucion.primer_trimestre < date.today() and date.today() < institucion.segundo_trimestre:
        # El segundo trimestre está en curso
        estado_primer_trimestre = calcular_estado_de_materia(materia, trimestre)
        estado_segundo_trimestre = calcular_estado_de_materia(materia, trimestre)
        estado_tercer_trimestre = 'fa fa-clock-o'
        habilitao_primer_trimestre = False
        habilitado_segundo_trimestre = True
        habilitado_tercer_trimestre = False

    elif institucion.segundo_trimestre < date.today() and date.today() < institucion.tercer_trimestre:
        # El tercer trimestre está en curso
        estado_primer_trimestre = calcular_estado_de_materia(materia, trimestre)
        estado_segundo_trimestre = calcular_estado_de_materia(materia, trimestre)
        estado_tercer_trimestre = calcular_estado_de_materia(materia, trimestre)
        habilitao_primer_trimestre = False
        habilitado_segundo_trimestre = False
        habilitado_tercer_trimestre = True

    else:
        # El ciclo lectivo culminó
        estado_primer_trimestre = calcular_estado_de_materia(materia, trimestre)
        estado_segundo_trimestre = calcular_estado_de_materia(materia, trimestre)
        estado_tercer_trimestre = calcular_estado_de_materia(materia, trimestre)
        habilitao_primer_trimestre = False
        habilitado_segundo_trimestre = False
        habilitado_tercer_trimestre = False

    estados = { '1':{'1':estado_primer_trimestre,'2':estado_segundo_trimestre,'3':estado_tercer_trimestre},
                '2':{'1':habilitao_primer_trimestre, '2':habilitado_segundo_trimestre, '3':habilitado_tercer_trimestre}
              }
    return estados[str(clave)][str(trimestre)]

# --------- fin de filtros --------------


# Funciones helpers


def calcular_estado_de_materia(materia, trimestre):
    '''
    :param materia: Una materia
    :param trimestre: 1,2 o 3
    :return: Chequea si están cargadas todas las notas de esa materia para ese trimestre y según corresponda retorna check o fail.
    '''
    return 'fa fa-check'

# ----------- fin funciones helpers -------------



class ManualView(View):

    def get(self, request):
        return render(request, 'manual.html')


class Dudas_profesorView(View):

    def get(self, request):
        preguntas = Preguntas_Profesor.objects.all()
        return render(request, 'dudas_profesor.html', {'preguntas': preguntas})


class Dudas_administradorView(View):

    def get(self, request):
        preguntas = Preguntas_Administrador.objects.all()
        return render(request, 'dudas_administrador.html', {'preguntas' : preguntas})


class Preguntas_frecuentesView(View):

    def get(self, request):
        preguntas = Preguntas_Frecuentes.objects.all()
        return render(request, 'preguntas_frecuentes.html', {'preguntas': preguntas})


class LoginView(View):

    def get(self, request):
        if request.user.is_authenticated():
            return redirect('materias_de_docente')
        else:
            form = LoginForm()
            nombre_institucion = get_institucion_name()
            return render(request, 'login.html', {'form': form, 'nombre_institucion': nombre_institucion})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=User.objects.get(username= request.POST['username']), password=request.POST['password'])
            login(request, user)
            return redirect('materias_de_docente')
        else:
            return render(request, 'login.html', {'form': form})

class DocenteChangePasswordView(View):

    @method_decorator(login_required)
    def get(self, request):
        form = ChangePasswordForm()
        return render(request, 'change_password.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = request.POST['password_1']
            user_logged = User.objects.get(username=request.user.username)
            user_logged.set_password(new_password)
            user_logged.save()
            return redirect('login')
        else:
            return render(request, 'change_password.html', {'form': form})

class DocenteResetPasswordView(View):

    def get(self, request):
        return render(request, 'reset_password.html')

class DocenteMateriasView(View):

    @method_decorator(login_required)
    def get(self, request):
        materias = Materia.objects.filter(usuarios__id=request.user.id)
        return render(request, 'materias.html', {'nombre_institucion': get_institucion_name(), 'user': request.user, 'materias': materias})

class LogOutView(View):

    @method_decorator(login_required)
    def get(self, request):
        logout(request)
        return redirect('login')


class CursosView(View):
    def get(self, request):
        return render(request, 'pantalla_cursos.html')

def get_institucion_name():
    institucion = Institucion.objects.all()
    if institucion:
        nombre_institucion = institucion[0].nombre
    else:
        nombre_institucion = "Nombre a completar"
    return nombre_institucion