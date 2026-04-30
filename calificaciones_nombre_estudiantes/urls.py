from django.urls import path
from django.contrib.auth import views as auth_views

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
    path(
        'recuperar-contrasena/',
        auth_views.PasswordResetView.as_view(
            template_name='calificaciones/password_reset_form.html',
            email_template_name='calificaciones/password_reset_email.html',
            subject_template_name='calificaciones/password_reset_subject.txt',
            success_url='enviado/',
        ),
        name='password_reset',
    ),
    path(
        'recuperar-contrasena/enviado/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='calificaciones/password_reset_done.html',
        ),
        name='password_reset_done',
    ),
    path(
        'recuperar-contrasena/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='calificaciones/password_reset_confirm.html',
            success_url='/recuperar-contrasena/completado/',
        ),
        name='password_reset_confirm',
    ),
    path(
        'recuperar-contrasena/completado/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='calificaciones/password_reset_complete.html',
        ),
        name='password_reset_complete',
    ),
]
