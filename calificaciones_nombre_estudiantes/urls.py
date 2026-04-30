from django.urls import path

from .views import (
    crear_calificacion,
    editar_calificacion,
    eliminar_calificacion,
    listar_calificaciones,
    login_view,
    logout_view,
    promedio_general,
    registro,
)

urlpatterns = [
    path('', listar_calificaciones, name='listar'),
    path('crear/', crear_calificacion, name='crear'),
    path('editar/<int:id>/', editar_calificacion, name='editar'),
    path('eliminar/<int:id>/', eliminar_calificacion, name='eliminar'),
    path('promedio-general/', promedio_general, name='promedio_general'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registro/', registro, name='registro'),
]
