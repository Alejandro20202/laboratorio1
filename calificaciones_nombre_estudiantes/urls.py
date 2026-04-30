from django.urls import path

from .views import (
    crear_calificacion,
    editar_calificacion,
    eliminar_calificacion,
    listar_calificaciones,
    promedio_general,
)

urlpatterns = [
    path('', listar_calificaciones, name='listar'),
    path('crear/', crear_calificacion, name='crear'),
    path('editar/<int:id>/', editar_calificacion, name='editar'),
    path('eliminar/<int:id>/', eliminar_calificacion, name='eliminar'),
    path('promedio-general/', promedio_general, name='promedio_general'),
]
