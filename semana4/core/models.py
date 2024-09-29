from django.db import models

# Create your models here.

class Cliente (models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    ciudad = models.CharField(max_length=100)
    edad = models.IntegerField()
    fono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre
    
class Juego (models.Model):
    Id_categoria = models.IntegerField()
    descripcion_juego = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion_juego

class Deporte (models.Model):
    Id_juego = models.IntegerField()


    def __str__(self):
        return self.Id_juego

class aventura (models.Model):
    Id_juego = models.IntegerField()

    def __str__(self):
        return self.Id_juego
    
class Infantiles (models.Model):
    Id_juego = models.IntegerField()
    
    def __str__(self):
        return self.Id_juego

class Estrategia (models.Model):
    Id_juego = models.IntegerField()
    
    def __str__(self):
        return self.Id_juego

