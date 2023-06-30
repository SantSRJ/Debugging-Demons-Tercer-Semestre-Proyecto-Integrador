from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator


class Servicios(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)] 
    )
    img= models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = 'servicios'
        verbose_name = "Servicio"

    def __str__(self):
        return f'''
            {self.nombre},
            {self.descripcion},
            {self.precio}        
        '''
