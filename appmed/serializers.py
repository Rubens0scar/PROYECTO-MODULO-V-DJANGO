from rest_framework import serializers
from .models import Paciente
from .models import Consulta
from .models import Diagnostico
from .models import Examenes
from .models import Tratamiento
from .models import Medicamentos

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = "__all__"

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = "__all__"

class DiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostico
        fields = "__all__"

class ExamenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examenes
        fields = "__all__"

class TratamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamiento
        fields = "__all__"

class MedicamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamentos
        fields = "__all__"