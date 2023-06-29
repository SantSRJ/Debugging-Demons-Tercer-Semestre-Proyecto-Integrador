from django.db import models

from Usuarios.models import Usuario
from Servicios.models import Servicios

# Create your models here.
class Turno(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models. CASCADE)
    profesional = models.ForeignKey(Usuario, on_delete=models. CASCADE, related_name="turno_profesional")
    servicio = models.ForeignKey(Servicios, on_delete=models. CASCADE)
    detalle = models.CharField(max_length=200)
    fechaHora = models.DateTimeField()

    def __str__(self) -> str:
        return f'''
            Cliente: {self.cliente},
            Profesional: {self.profesional},
            Servicio: {self.servicio},
            Fecha: {self.fechaHora}        
        '''
