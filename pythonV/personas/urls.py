from django.urls import path
from . import views

urlpatterns = [
    path('', views.reporte_personas, name='reporte_personas'), # La raíz de la app mostrará el reporte
    path('registrar/', views.registrar_persona, name='registrar_persona'),
     path('editar/<int:pk>/', views.editar_persona, name='editar_persona'),
     path('eliminar/<int:pk>/', views.eliminar_persona, name='eliminar_persona'),
]
