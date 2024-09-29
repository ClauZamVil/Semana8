from django.urls import path
from .import views

urlpatterns = [
    path ('cliente', views.lista_cliente, name="lista_cliente"),
    path ('cliente/<id_cliente>', views.vista_cliente, name="vista_cliente")
]