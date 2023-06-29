from django import forms
from .models import Turno

class fromularioAltaTurno(forms.Form):
    
        profesional =  forms.ComboField()
        servicio =  forms.ComboField()
        fechaHora = forms.DateTimeField()
        
        
        class Meta:
            model = Turno
