from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.views import ImprimirBoletinesView, ExportarCursoView, ExamenBorrarView, ExamenNuevoView, ExamenesAlumnoView, LoginView, DocenteResetPasswordView, DocenteMateriasView, Dudas_profesorView, LogOutView,Dudas_administradorView, Preguntas_frecuentesView, DocenteChangePasswordView, ManualView, Dudas_profesorView, CursosView, EstadisticasView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', LoginView.as_view(), name='login'),
    url(r'^logout/', LogOutView.as_view(), name='logout'),
    url(r'^reset_password', DocenteResetPasswordView.as_view(), name='reset_password'),
    url(r'^change_password', DocenteChangePasswordView.as_view(), name='change_password'),
    url(r'^materias', DocenteMateriasView.as_view(), name='materias_de_docente'),
    url(r'^cursos/(?P<materia_pk>\w+)/(?P<trimestre>\w+)', CursosView.as_view(), name='cursos'),
    url(r'^manual', ManualView.as_view(), name='manual'),
    url(r'^estadisticas', EstadisticasView.as_view(), name='estadisticas'),
    url(r'^dudas_profesor', Dudas_profesorView.as_view(), name='dudas_profesor'),
    url(r'^dudas_administrador', Dudas_administradorView.as_view(), name='dudas_administrador'),
    url(r'^preguntas_frecuentes', Preguntas_frecuentesView.as_view(), name='preguntas_frecuentes'),
    url(r'^examenes_alumno', ExamenesAlumnoView.as_view(), name='examenes_alumno'),

    url(r'^examen/nuevo', ExamenNuevoView.as_view(), name='examen_nuevo'),
    url(r'^examen/borrar', ExamenBorrarView.as_view(), name='examen_borrar'),

    url(r'^exportar/curso', ExportarCursoView.as_view(), name='exportar_curso'),

    url(r'^imprimir/boletines', ImprimirBoletinesView.as_view(), name='imprimir_boletines'),
)