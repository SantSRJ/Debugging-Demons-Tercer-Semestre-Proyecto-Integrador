from django.shortcuts import render
from .forms import modificarServicioForm

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

def eliminarServicio(request, id): #Del
    servicios = get_object_or_404(Servicios, idServicio=id)

    if request.method == 'POST':
        servicios.delete()
        return redirect('mostrar_servicio')
    return render(request, 'mostrar_servicio.html', {'servicios': servicios})



def modificarServicio(request, id):
    
    if request.method == 'POST':
        form = modificarServicioForm(request.POST)
        if form.is_valid():
            servicios.precio = form.cleaned_data['precio']
            servicios.descripcion = form.cleaned_data['descripcion']
            
            if form.cleaned_data['nombre']:
                servicios.nombre = form.cleaned_data['nombre']
            
            servicios.save()
            return redirect('servicios')
    else:
        form = modificarServicioForm(initial={
            'nombre': servicios.nombre,
            'precio': servicios.precio,
            'descripcion': servicios.descripcion,
        })
    
    return render(request, 'modificar_servicio.html', {'form': form})


