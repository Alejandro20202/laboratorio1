from django.shortcuts import render
from django.db.models import Avg

from .models import Calificacion


def promedio_general(request):
    promedio = Calificacion.objects.all().aggregate(Avg('promedio'))['promedio__avg']
    return render(request, 'calificaciones/promedio.html', {'promedio': promedio})
