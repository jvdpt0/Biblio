from django.urls import path

from . import views

urlpatterns = [
    path('', views.PaginaInicialView.as_view(), name='index'),
    path('cadastrar-livro', views.AdicionarLivroView.as_view(), name='cadastrar-livro'),
    path('lista-livros', views.ListaLivrosView.as_view(), name='lista-livros'),
]
