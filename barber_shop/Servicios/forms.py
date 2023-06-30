from django import forms
from .models import Servicios
    
class formularioServicio(forms.Form):
    nombre = forms.CharField(max_length=100)
    precio = forms.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    descripcion = forms.CharField(max_length=255)
    img= forms.CharField(max_length=100)

    class Meta:
            model = Servicios
            
class modificarServicioForm(forms.Form):
    nombre = forms.CharField(required=False)
    precio = forms.IntegerField(required=True)
    descripcion = forms.CharField(required=True, widget=forms.Textarea) 