from django.forms import ModelForm
from .models import Pregrado

class PregradoForm(ModelForm):
    class Meta:
        model = Pregrado
        fields = ['cod_pregrado', 'cod_sede', 'region', 'nombre', 'creditos', 'nota_minima']