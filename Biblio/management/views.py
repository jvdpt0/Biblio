from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth import views as auth_views

from .models import ModelLivro, ModelUsuario, ModelFavoritos
from .forms import FormCriarUsuario


# Create your views here.

class PaginaInicialView(TemplateView):
    template_name = 'management/index.html'

class AdicionarLivroView(CreateView):
    template_name = 'management/cadastrar_livro.html'
    model = ModelLivro
    fields = ['nome', 'autor', 'foto']
    success_url = '/'

class ListaLivrosView(ListView):
    template_name = 'management/lista_livros.html'
    model = ModelLivro
    ordering = ['nome']
    context_object_name = 'livros'

class RegistrarView(CreateView):
    model = ModelUsuario
    template_name = 'management/registrar.html'
    form_class = FormCriarUsuario
    success_url = '/login/'

class LivrosFavoritos(ListView):
    model = ModelFavoritos
    template_name = 'management/livros_favoritos.html'
    context_object_name = 'livros_favoritos'

    def get_queryset(self):
        return ModelFavoritos.objects.filter(usuario=self.request.user)