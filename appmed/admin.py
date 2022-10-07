from django.contrib import admin

from .models import Diagnostico
from .models import Paciente
from .models import Consulta
from .models import Examenes
from .models import Tratamiento
from .models import Medicamentos


class PacienteAdmin(admin.ModelAdmin):
    list_display = ("codigo","nombre","apellido")
    ordering = ["codigo"]
    search_fields = ["nombre"]

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ("id_paciente","motivo_consulta","fecha_atencion","hora_atencion")
    search_fields = ["nombre"]

class DiagnosticoAdmin(admin.ModelAdmin):
    list_display = ("id_consulta","nombre_diag","descripcion_diag")
    search_fields = ["nombre_diag"]

admin.site.register(Paciente,PacienteAdmin)
admin.site.register(Consulta,ConsultaAdmin)
admin.site.register(Diagnostico,DiagnosticoAdmin)

admin.site.register(Examenes)
admin.site.register(Tratamiento)
admin.site.register(Medicamentos)