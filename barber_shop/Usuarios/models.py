from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):

    telefono = models.CharField(max_length=25)
    esBarbero = models.BooleanField(default=False) # True o False
    direccion = models.CharField(max_length=50)
    img = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50, default='123456abc!')
    username = models.CharField(max_length=50, default='username', unique=True)
    
    def __str__(self):
        return f'''
            {self.first_name} 
            {self.last_name}       
        '''

    
