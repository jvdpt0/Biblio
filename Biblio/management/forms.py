from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ModelUsuario

class FormCriarUsuario(UserCreationForm):
    class Meta:
        model = ModelUsuario
        fields = ['nome', 'sobrenome', 'username', 'email', 'foto_de_perfil']
        