from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationform
from django.contrib.auth.decorators import login_required
from .forms import RegistroClienteForm




# Create your views here.

def index(request):
    if request.method == 'POST':
        form =RegistroClienteForm (request.POST)
        if form.is_valid():
            form.save()
        return render(request,'core/index.html')    
    else:
        form = RegistroClienteForm()
    
    contexto = {
        'form': form,
        'cliente': request.user
    }
    return render(request,'core/index.html',contexto)
    
def CategoriaAventura(request):
    return render(request, 'core/CategoriaAventura.html')

def Aventura1(request):
    return render(request, 'core/Aventura1.html')

def Aventura2(request):
    return render(request, 'core/Aventura2.html')

def CategoriaConduccion(request):
    return render(request, 'core/CategoriaConduccion.html')

def categoriaDeportes(request):
    return render(request, 'core/categoriaDeportes.html')

def CategoriaEstrategia(request):
    return render(request, 'core/CategoriaEstrategia.html')

def CategoriaInfantiles(request):
    return render(request, 'core/CategoriaInfantiles.html')

def Conduccion1(request):
    return render(request, 'core/Conduccion1.html')

def Conduccion2(request):
    return render(request, 'core/Conduccion2.html')

def Deporte1(request):
    return render(request, 'core/Deporte1.html')

def Deporte2(request):
    return render(request, 'core/Deporte2.html')

def Estrategia1(request):
    return render(request, 'core/Estrategia1.html')

def Estrategia2(request):
    return render(request, 'core/Estrategia2.html')

def Infantil1(request):
    return render(request, 'core/Infantil1.html')

def Infantil2(request):
    return render(request, 'core/Infantil2.html')


def Principal(request):
    return render(request, 'core/Principal.html')

def recuperar_contrasena(request):
    return render(request, 'core/recuperar_contrasena.html')

def register(request):
    return render(request, 'core/register.html')

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'core/login.html'
    authentication_form = CustomAuthenticationform
    redirect_authenticated_user = True