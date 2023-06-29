from django.shortcuts import render
from datetime import datetime

from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.


def home(request):
    return render(request, 'home.html',{'mensaje': 'Explora nuestros Servicios'})

@login_required(login_url='login')
def turnos(request):
    
    user = request.user
    turnos = Turno.objects.filter(cliente = user)
    profesionales = Usuario.objects.filter(esBarbero=True)
    servicios = Servicios.objects.all()

    if request.user.is_authenticated:
        return render(request, 'turnos.html',{'turnos': turnos,
                                              'servicios': servicios,
                                              'profesionales': profesionales,
                                              'vacio': 'No tiene turnos'})

@login_required(login_url='login')
def nuevoTurno(request):
    
    
    if request.POST:
        
        profesional = request.POST.get('profesional')
        servicio = request.POST.get('servicio')
        fechaHora = request.POST['fechaHora']
        fecha_datetime = datetime.strptime(fechaHora, "%Y-%m-%dT%H:%M")
        
        turno =  Turno(None,
                    request.user.id,
                    profesional,
                    servicio,
                    "",
                    fecha_datetime)
        turno.save()
        
        turnos = Turno.objects.filter(cliente = request.user)
        return render(request, 'turnos.html',{'turnos': turnos})
        
    
    servicios = Servicios.objects.all()
    profesionales = Usuario.objects.filter(esBarbero=True)
    
    return render(request, 'altaTurno.html',{'profesionales': profesionales, 'servicios': servicios})


def acercaDe(request):
        return render(request, 'acercaDe.html')
    
    
    
def eliminarTurno(request, id):
    Turno.objects.filter(pk=id).delete()
    mensaje = "Turno eliminado."
    turnos =  Turno.objects.all()
    return render (request, 'turnos.html',{'turnos':turnos, 'mensaje':mensaje})
    