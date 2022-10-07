from django.core.exceptions import ValidationError

def validar_codigo_paciente(value):
    if len(value) != 9:
        raise ValidationError('El codigo debe contener 9 caracteres.')

def validar_codigo(value):
    if not value.startswith("PAC-"):
        raise ValidationError("El codigo debe empezar con PAC-")

def validar_motivo(value):
    if len(value) < 15:
        raise ValidationError("Debe detallar el motivo de la consulta del Paciente, minimo debe tener 20 caracteres")

def validar_talla(value):
    if value<20:
        raise ValidationError("El paciente debe medir mas de 20 centimetros.")

def validar_peso(value):
    if value<1.5:
        raise ValidationError("El paciente debe pesar por lo menos 1.5 kilos.")

def validar_nombre(value):
    if len(value)<10:
        raise ValidationError("Debe ingresar un nombre adecuado al diagnostico echo, minimo de 12 caracteres.")

def validar_descripcion(value):
    if len(value)<20:
        raise ValidationError("Debe ingresar una descripcion detallada del diagnostico echo, minimo de 23 caracteres.")

def validar_detalle_examen(value):
    if len(value)<10:
        raise ValidationError("Debe ingresar el detalle adecuado del examen, minimo de 12 caracteres.")

def validar_resultado_axamen(value):
    if len(value)<20:
        raise ValidationError("Debe ingresar el resultado detallado del examen echo, minimo de 23 caracteres.")

def validar_tratamiento(value):
    if len(value)<10:
        raise ValidationError("Debe ingresar el tratamiento detallado, minimo de 12 caracteres.")

def validar_dieta_tratamiento(value):
    if len(value)<10:
        raise ValidationError("Debe ingresar una descripcion detallada del diagnostico echo si corresponde, minimo de 7 (ninguno) caracteres.")

def validar_codigo_medicamento(value):
    if len(value) != 10:
        raise ValidationError('El codigo debe contener 10 caracteres.')

def validar_codigo_sigla(value):
    if not value.startswith("MED-"):
        raise ValidationError("El codigo debe empezar con MED-")

def validar_nombre_medicamento(value):
    if len(value)<10:
        raise ValidationError("Debe ingresar el nombre correcto del medicamento.")

def validar_detalle_medicamento(value):
    if len(value)<10:
        raise ValidationError("Debe ingresar el detalle de la receta que corresponde al medicamento.")
