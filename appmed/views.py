from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import api_view
from .models import Paciente
from .models import Consulta
from .models import Diagnostico
from .models import Examenes
from .models import Tratamiento
from .models import Medicamentos
from .serializers import PacienteSerializer
from .serializers import ConsultaSerializer
from .serializers import DiagnosticoSerializer
from .serializers import ExamenesSerializer
from .serializers import TratamientoSerializer
from .serializers import MedicamentosSerializer


def index(request):
    return HttpResponse("Hola mundo")

#PARA ModelViewSet
class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

class DiagnosticoViewSet(viewsets.ModelViewSet):
    queryset = Diagnostico.objects.all()
    serializer_class = DiagnosticoSerializer

class ExamenesViewSet(viewsets.ModelViewSet):
    queryset = Examenes.objects.all()
    serializer_class = ExamenesSerializer

class TratamientoViewSet(viewsets.ModelViewSet):
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer

class MedicamentosViewSet(viewsets.ModelViewSet):
    queryset = Medicamentos.objects.all()
    serializer_class = MedicamentosSerializer

#GENERIC API
class PacienteCreateAndList(generics.CreateAPIView,generics.ListAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

#Custom API
@api_view(["GET"])
def paciente_contador(request):
    """
    Cantidad de pacientes registrados
    """

    try:
        cantidad = Paciente.objects.count()
        return JsonResponse(
            {
                "Cantidad de Pacientes Registrados": cantidad,
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje: ": str(e)},status=400)


@api_view(["GET"])
def paciente_cantidad_consultas(request,id):
    """
    Cantidad de consultas que tuvo un paciente dado
    """
    # id = request.query_params["id"]
    datapaciente = Paciente.objects.get(pk=id)
    cantidadconsultas = Consulta.objects.filter(id_paciente=id).count()
    try:
        return JsonResponse(
            {
                "Paciente": datapaciente.codigo + ' - ' + datapaciente.nombre + ' ' + datapaciente.apellido,
                "Cantidad Consultas: ": cantidadconsultas,
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje: ": str(e)},status=400)