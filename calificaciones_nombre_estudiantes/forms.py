from django.forms import ModelForm

from .models import Calificacion


class CalificacionForm(ModelForm):
    class Meta:
        model = Calificacion
        exclude = ['promedio']
