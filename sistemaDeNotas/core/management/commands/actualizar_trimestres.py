from django.core.management.base import BaseCommand
from core.models import *
import datetime
from core.views import actualizar_promedios

class Command(BaseCommand):

    # args [0] -> cursada . Ej: 1, 2, 3, 4, 5, 6, 7
    def handle(self, *args, **options):
        materias = Materia.objects.filter(seccion__cursada=args[0])
        for materia in materias:
            print "actualizando ... " + materia.nombre + ' | ' + str(materia.seccion)
            alumnos_inscriptos = map(lambda i: i.alumno, filter(lambda i : i.fecha_baja == None or i.fecha_baja> datetime.datetime.now().date(), Inscripcion.objects.filter(seccion=materia.seccion)))
            trimestres = [1, 2, 3]
            for alumno in alumnos_inscriptos:
                for trimestre in trimestres:
                    #print "actualizando ... " + str(alumno.dni) + ' | ' + materia.nombre + ' | ' + str(trimestre)
                    actualizar_promedios(alumno, materia, trimestre)

    def add_arguments(self, parser):
        parser.add_argument('args')


