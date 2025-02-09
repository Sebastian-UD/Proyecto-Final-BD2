from django.contrib import admin
from .models import Sede, Pregrado, Asignatura, Curso, Grupo, Clasificacion, Profesor, Dicta, Nomina

# Register your models here.
admin.site.register(Sede)
admin.site.register(Pregrado)
admin.site.register(Asignatura)
admin.site.register(Curso)
admin.site.register(Grupo)
admin.site.register(Clasificacion)
admin.site.register(Profesor)
admin.site.register(Dicta)
admin.site.register(Nomina)