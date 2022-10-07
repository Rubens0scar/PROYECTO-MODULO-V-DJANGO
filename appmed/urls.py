from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register(r"paciente",views.PacienteViewSet)
router.register(r"consulta",views.ConsultaViewSet)
router.register(r"diagnostico",views.DiagnosticoViewSet)
router.register(r"examenes",views.ExamenesViewSet)
router.register(r"tratamiento",views.TratamientoViewSet)
router.register(r"medicamentos",views.MedicamentosViewSet)


urlpatterns = [
    # ath("",views.index, name="index")
    
    path('paciente/create_list',views.PacienteCreateAndList.as_view(),name='pacientes'),
    path('paciente/cantidad',views.paciente_contador),
    path('paciente/cantidad_consultas/<int:id>',views.paciente_cantidad_consultas),
    path('',include(router.urls))
]
