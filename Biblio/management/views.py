from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth import views as auth_views


from .models import ModelLivro, ModelUsuario, ModelFavoritos, ModelAnalise
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

class LivrosFavoritosView(ListView):
    model = ModelFavoritos
    template_name = 'management/livros_favoritos.html'
    context_object_name = 'favorito'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        livros_favoritos = ModelFavoritos.objects.filter(usuario=self.request.user)
        context['livros_favoritos'] =livros_favoritos
        return context

    def get_queryset(self):
        return ModelFavoritos.objects.filter(usuario=self.request.user)
    
class LivroDetalhadoView(DetailView):
    model = ModelLivro
    template_name = 'management/livro_detalhado.html'
    context_object_name = 'livro'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        analises = ModelAnalise.objects.filter(livro=self.object)
        context['analises'] = analises
        return context
    
    def post(self, request, *args, **kwargs):
        livro_id = kwargs['pk']
        livro = get_object_or_404(ModelLivro, pk=livro_id)
        nota = request.POST.get('nota')
        analise = request.POST.get('analise')

        if nota and analise:
            avaliacao = ModelAnalise(
                usuario=request.user,
                livro=livro,
                analise=analise,
                nota=nota,
            )
            avaliacao.save()

        return redirect('livro-detalhado', pk=livro_id)