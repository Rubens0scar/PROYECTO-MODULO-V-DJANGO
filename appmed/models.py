from django.db import models
from django.conf import settings
from .validators import validar_codigo_paciente
from .validators import validar_codigo
from .validators import validar_motivo
from .validators import validar_talla
from .validators import validar_peso
from .validators import validar_nombre
from .validators import validar_descripcion
from .validators import validar_detalle_examen
from .validators import validar_resultado_axamen
from .validators import validar_tratamiento
from .validators import validar_dieta_tratamiento
from .validators import validar_codigo_medicamento
from .validators import validar_codigo_sigla
from .validators import validar_nombre_medicamento
from .validators import validar_detalle_medicamento

class GeneroUnits(models.TextChoices):
    M = 'm', 'Masculino'
    F = 'f', 'Femenino'
	
class PagoUnits(models.TextChoices):
    EFE = 'e', 'Efectivo'
    SEG = 's', 'Asegurado'

class ExamenUnits(models.TextChoices):
    SAN = 's', 'Sangre'
    OR = 'o', 'Orina'
    HE = 'h', 'Heces'
    RA = 'r', 'Rayos X'
    EC = 'e', 'Ecografia'

class TipoMedicamentoUnits(models.TextChoices):
    FR = 'f','Frasco'
    PA = 'p', 'Pastillas'
    JE = 'j', 'Jeringas'
    Su = 's', 'Suero'
    AM = 'a', 'Ampollas'

class CivilUnits(models.TextChoices):
    SO = 's', 'Soltero/a'
    CA = 'c', 'Casado/a'
    OT = 'o', 'Otro'
		
class Paciente(models.Model):
	codigo = models.CharField(max_length = 35, validators=[validar_codigo_paciente,validar_codigo])
	nombre = models.CharField(max_length = 35)
	apellido = models.CharField(max_length = 35)
	genero = models.CharField(
		max_length = 35,
		choices=GeneroUnits.choices,
        default=GeneroUnits.M
	)
	email = models.CharField(max_length = 35)
	municipio = models.CharField(max_length = 35)
	edad = models.IntegerField(default=1)
	estado_civil =  models.CharField(
		max_length = 35,
		choices=CivilUnits.choices,
        default=CivilUnits.SO
	)
	telefono = models.CharField(max_length = 25)
	direccion = models.CharField(max_length = 25)
	nivel_educativo = models.CharField(max_length = 50)
	ocupacion = models.CharField(max_length = 25)
	def __str__(self):
		return self.codigo + ': ' + self.nombre + ' ' + self.apellido

class Consulta(models.Model):
    id_paciente = models.ForeignKey(Paciente, null = False, blank = False, on_delete = models.CASCADE)
    motivo_consulta = models.CharField(max_length = 800, validators=[validar_motivo,])
    fecha_atencion = models.DateField(auto_now_add=True)
    hora_atencion = models.TimeField(auto_now_add=True)
    consulta_pago = models.CharField(max_length = 35,choices=PagoUnits.choices,default=PagoUnits.EFE)
    peso = models.DecimalField(decimal_places=2, max_digits=6, validators=[validar_peso,])
    estatura = models.DecimalField(decimal_places=2, max_digits=8, validators=[validar_talla,])
    fecha_proxima_consulta = models.DateField()
    def __str__(self):
        return 'Paciente:' + str(self.id_paciente) + ' - ' + self.motivo_consulta
    
	
class Diagnostico(models.Model):
    id_consulta = models.ForeignKey(Consulta, null = False, blank = False, on_delete = models.CASCADE)
    nombre_diag= models.CharField(max_length=400,validators=[validar_nombre,])
    descripcion_diag= models.TextField(max_length=1000,validators=[validar_descripcion,])
    def __str__(self):
        return self.nombre_diag
    
	
class Examenes(models.Model):
    id_consulta = models.ForeignKey(Consulta, null = False, blank = False, on_delete = models.CASCADE)
    tipo_examen = models.CharField(max_length = 35,choices=ExamenUnits.choices,default=ExamenUnits.SAN)
    detalle_examen = models.TextField(max_length = 1000, validators=[validar_detalle_examen,])
    resultado_examen = models.TextField(max_length = 1000, validators=[validar_resultado_axamen,])
    def __str__(self):
        return str(self.id_consulta) + ' Tipo: ' + self.tipo_examen
    
	
class Tratamiento(models.Model):
    id_consulta = models.ForeignKey(Consulta, null = False, blank = False, on_delete = models.CASCADE)
    id_diagnostico = models.ForeignKey(Diagnostico, null = False, blank = False, on_delete = models.CASCADE)
    tratamiento = models.TextField(max_length = 1000,validators=[validar_tratamiento,])
    dieta = models.TextField(max_length = 1000, validators=[validar_dieta_tratamiento,])
    def __str__(self):
        return str(self.id_consulta) + ' - ' + str(self.id_diagnostico)
    
	
class Medicamentos(models.Model):
    id_tratamiento = models.ForeignKey(Tratamiento, null = False, blank = False, on_delete = models.CASCADE)
    codigo_medicamento = models.CharField(max_length = 100,validators=[validar_codigo_medicamento,validar_codigo_sigla,])
    nombre_medicamento = models.CharField(max_length = 500,validators=[validar_nombre_medicamento,])
    cantidad = models.IntegerField(default=1)
    tipo_medicamento = models.CharField(max_length = 35,choices=TipoMedicamentoUnits.choices,default=TipoMedicamentoUnits.FR)
    detalle = models.TextField(max_length = 1000,validators=[validar_detalle_medicamento,])
    def __str__(self):
        return str(self.id_tratamiento) + ' - ' + self.codigo_medicamento + ' - ' + self.nombre_medicamento
    
