from django.shortcuts import render, redirect, get_object_or_404
from .models import Pregrado
from .forms import PregradoForm
from sede.models import Sede

# Create your views here.
def get_pregrados(request):
    pregrados = list(Pregrado.objects.all())

    return render(request, 'pregrados.html', {
        'pregrados': pregrados
    })

def create_pregrado(request):
    if request.method=='GET':
        return render(request, 'create_pregrado.html', {
            'form': PregradoForm
        })
    else:
        codigo = request.POST['cod_pregrado']
        cod_sede = request.POST['cod_sede']
        nombre = request.POST['nombre']
        creditos = request.POST['creditos']
        nota = request.POST['nota_minima']

        sede = get_object_or_404(Sede, cod_sede=cod_sede)

        pregrado = Pregrado(cod_pregrado=codigo, cod_sede=sede, nombre=nombre, creditos=creditos, nota_minima=nota)
        pregrado.save()

        return redirect('get_pregrados')