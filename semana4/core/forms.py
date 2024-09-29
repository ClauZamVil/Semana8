from django import forms
from .models import Cliente
from django.contrib.auth.forms import AuthenticationForm

class RegistroClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'ciudad', 'edad', 'fono']

class CustomAuthenticationform(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Nombre de usuario',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'contraseña',
    }))
