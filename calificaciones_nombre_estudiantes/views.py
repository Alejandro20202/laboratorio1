from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Calificacion
from .forms import CalificacionForm


def registro(request):
    if request.user.is_authenticated:
        return redirect('listar')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('listar')
    else:
        form = UserCreationForm()

    return render(request, 'calificaciones/registro.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('listar')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('listar')
    else:
        form = AuthenticationForm()

    return render(request, 'calificaciones/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def listar_calificaciones(request):
    calificaciones = Calificacion.objects.all()
    promedio_general = Calificacion.objects.all().aggregate(Avg('promedio'))['promedio__avg']
    return render(request, 'calificaciones/listar.html', {
        'calificaciones': calificaciones,
        'promedio_general': promedio_general,
    })


@login_required(login_url='login')
def crear_calificacion(request):
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = CalificacionForm()

    return render(request, 'calificaciones/crear.html', {'form': form})


@login_required(login_url='login')
def editar_calificacion(request, id):
    calificacion = get_object_or_404(Calificacion, id=id)
    if request.method == 'POST':
        form = CalificacionForm(request.POST, instance=calificacion)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = CalificacionForm(instance=calificacion)

    return render(request, 'calificaciones/editar.html', {
        'form': form,
        'calificacion': calificacion,
    })


@login_required(login_url='login')
def eliminar_calificacion(request, id):
    calificacion = get_object_or_404(Calificacion, id=id)
    if request.method == 'POST':
        calificacion.delete()
        return redirect('listar')

    return render(request, 'calificaciones/eliminar.html', {'calificacion': calificacion})


@login_required(login_url='login')
def promedio_general(request):
    promedio = Calificacion.objects.all().aggregate(Avg('promedio'))['promedio__avg']
    return render(request, 'calificaciones/promedio.html', {'promedio': promedio})
