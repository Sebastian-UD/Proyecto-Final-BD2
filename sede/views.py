from django.shortcuts import render, redirect, get_object_or_404
from .models import Sede
from .forms import SedeForm

from django.http import HttpResponse

# Create your views here.
def get_sedes(request):
    sedes = list(Sede.objects.all())
    return render(request, 'sedes.html', {
        'sedes': sedes
    })
    
def create_sede(request):
    if request.method=='GET':
        return render(request, 'create_sede.html', {
            'form': SedeForm
        })
    else:
        form = SedeForm(request.POST)
        new_sede = form.save();
        return redirect('get_sedes')
    
def sede_detail(request, codigo):
    if request.method=='GET':
        sede = get_object_or_404(Sede, cod_sede=codigo)
        return render(request, 'sede_detail.html', {
            'sede': sede
        })
    else:
        sede = get_object_or_404(Sede, cod_sede=codigo)
        sede.nombre_sede = request.POST['nombre_sede']
        sede.save()
        return redirect('get_sedes')
    
def delete_sede(request, codigo):
    sede = get_object_or_404(Sede, cod_sede=codigo)
    sede.delete()
    return redirect('get_sedes')