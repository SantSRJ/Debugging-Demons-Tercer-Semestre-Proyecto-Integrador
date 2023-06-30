from django.shortcuts import render
from .forms import formularioDeLogin, formularioDeREgistro
from .models import Usuario

# Create your views here.
def login(request):
    form = formularioDeLogin
    return render(request, 'registration/login.html', {'form':form})


def registro(request):
    if request.POST:
              
        user =  request.POST['username']
        password =  request.POST['password']
        verificacion_password = request.POST['verificacion_password']
        nombre =  request.POST['nombre']
        apellido =  request.POST['apellido']
        email =  request.POST['email']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        imagen = request.POST['img']
        
        usuario  = Usuario.objects.create_user(
            user,
            email,
            password)
        usuario.first_name = nombre
        usuario.last_name = apellido
        usuario.direccion = direccion
        usuario.telefono = telefono
        usuario.img = imagen
    
        if request.user.is_staff:
            usuario.esBarbero = True
            usuario.is_staff = True
        else:
            usuario.esBarbero = False
            usuario.is_staff = False
        
        if(password == verificacion_password):
            usuario.save()
            return render(request,'registration/login.html')
        else:
            return render(request,'registration/registro.html',{'error': "Las contraseñas no coinciden"})
    
    form =  formularioDeREgistro
    return render(request,'registration/registro.html', {'form':form})


def perfil(request):
    return render(request, 'perfil.html')