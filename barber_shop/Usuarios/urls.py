from django.urls import path

from Usuarios import views
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    # (temlate, vista, nombre dentro de un html)
    
    path('login/', view=views.login, name='login'),
    path('registro/', view=views.registro, name='registro'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('perfil/', view=views.perfil , name='perfil'),
]