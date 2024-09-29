from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import RegistroClienteForm
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationform
# codigo para creae una url para la nueva visto info juegos pokemon
from django.urls import path
import requests

# pokemon_app/views.py

from django.shortcuts import render

def mostrar_lista_juegos(request):
    api_key = 'fb4fd79937fc41ccb5d9baf766aeb64e'  # Tu clave API RAWG
    url = f'https://api.rawg.io/api/games?platforms=18&key={api_key}'  # Obtener juegos de PlayStation (ID 18)
    response = requests.get(url)

    if response.status_code == 200:
        juegos_data = response.json().get('results', [])  # Obtener la lista de juegos
        juegos = []

        # Extraer información relevante
        for juego in juegos_data:
            juegos.append({
                'name': juego.get('name'),  # Nombre del juego
                'description': juego.get('description_raw', 'Sin descripción disponible'),  # Descripción
                'image': juego.get('background_image'),  # Imagen
                'released': juego.get('released'),  # Fecha de lanzamiento
                'rating': juego.get('rating'),  # Calificación
            })
    else:
        juegos = []  # Si hay un error, mostrar una lista vacía

    context = {
        'juegos': juegos,  # Pasar la lista de juegos al contexto
    }

    return render(request, 'core/lista_juegos.html', context) 



# API GIANTBOMB

def mostrar_video_shows(request):
    api_key = '4b23099b4ff44b373c9951590fd97acff1dd6161'  # Tu clave API
    url = f'https://www.giantbomb.com/api/video_shows/?api_key={api_key}&format=json&limit=10'  # Endpoint para obtener video shows
    response = requests.get(url)

    if response.status_code == 200:
        video_shows_data = response.json().get('results', [])
        video_shows = []

        # Extraer información relevante
        for show in video_shows_data:
            video_shows.append({
                'title': show.get('title', 'Sin título disponible'),  # Título del video show
                'description': show.get('deck', 'Sin descripción disponible'),  # Descripción
                'image': show.get('image', {}).get('small_url', 'https://via.placeholder.com/200'),  # Imagen
                'url': show.get('site_detail_url', '#'),  # URL del video show
                'latest_episode': show.get('latest', {}).get('title', 'Sin episodios disponibles'),  # Último episodio
            })
    else:
        video_shows = []  # Si hay un error, mostrar una lista vacía

    context = {
        'video_shows': video_shows,  # Pasar la lista de video shows al contexto
    }

    return render(request, 'core/video_shows.html', context)
# OTRAS VIEWS

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

def login(request):
    return render(request, 'core/login.html')

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