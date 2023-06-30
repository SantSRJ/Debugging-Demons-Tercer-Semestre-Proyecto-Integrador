from django.shortcuts import render, redirect
from .forms import modificarServicioForm
from .models import Servicios

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Servicios

# Create your views here.

def nuevo_servicio(request):
    if request.POST:
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        descripcion = request.POST['descripcion']
        imagen = request.POST['imagen'].get()

        servicio = Servicios(nombre=nombre, precio=precio, descripcion=descripcion, imagen=imagen)
        servicio.save()
    return render(request, 'altaServicio.html')


def mostrarServicio(request):
    servicios = Servicios.objects.all()
    return render(request, 'servicios.html', {'servicios': servicios, 'mensaje': "No hay Servicios"})


def eliminarServicio(request, id):
    Servicios.objects.filter(pk=id).delete()
    mensaje = "Servicio eliminado."
    servicios =  Servicios.objects.all()
    return render (request, 'turnos.html',{'turnos':servicios, 'mensaje':mensaje})


def mostrarFormularioServicio(request, id):
    
    servicio=  Servicios.objects.only(id =id)
    return render(request, 'altaServicio.html', {'servicio':servicio})
    
    pass


def modificarServicio(request, id):
    
    if request.method == 'POST':
            nombre = request.POST['nombre']
            descripcion = request.POST['direccion']
            precio = request.POST['precio']
            img = request.POST['img']
            
            servicio =  Servicios(id=id,nombre=nombre, precio=precio, descripcion=descripcion, imagen=img)
            
            servicio.save()
            
            return redirect('servicios')

