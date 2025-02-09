from django.forms import ModelForm
from django import forms
from .models import Sede

class SedeForm(ModelForm):
    class Meta:
        model = Sede
        fields = ['cod_sede', 'nombre_sede']