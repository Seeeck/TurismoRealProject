from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Zona)


class DepartamentoAdmin(admin.ModelAdmin):
    list_display=(
        'id_departamento',
        'nombre_departamento',
        'imagen_departamento',
        'numero_personas',
        'valor_dia',
        'estado_departamento',
        'id_zona',
    )
    search_fields=(
        'nombre_departamento',
    )
    list_filter=('id_zona',)

admin.site.register(Departamento,DepartamentoAdmin)
admin.site.register(Reserva)
