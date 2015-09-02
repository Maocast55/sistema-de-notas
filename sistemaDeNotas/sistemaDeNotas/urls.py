from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.views import LoginView, DocenteResetPasswordView, DocenteMateriasView, Dudas_profesorView, LogOutView, DocenteChangePasswordView, ManualView, ProfesorView, CursosView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', LoginView.as_view(), name='login'),
    url(r'^logout/', LogOutView.as_view(), name='logout'),
    url(r'^reset_password', DocenteResetPasswordView.as_view(), name='reset_password'),
    url(r'^change_password', DocenteChangePasswordView.as_view(), name='change_password'),
    url(r'^materias', DocenteMateriasView.as_view(), name='materias_de_docente'),
    url(r'^profesor', ProfesorView.as_view(), name='profesor'),
    url(r'^cursos', CursosView.as_view(), name='cursos'),
    url(r'^manual', ManualView.as_view(), name='manual'),
    url(r'^dudas_profesor', Dudas_profesorView.as_view(), name='dudas_profesor'),

)