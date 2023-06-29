from django.urls import path
from Servicios import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    # (temlate, vista, nombre dentro de un html)
    path('', view=views.mostrarServicio, name='servicios'),
    path('nuevo_servicio/', view=views.nuevo_servicio, name='nuevo_servicio'),
]