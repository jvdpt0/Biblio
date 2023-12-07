from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', views.PaginaInicialView.as_view(), name='index'),
    path('cadastrar-livro', login_required(views.AdicionarLivroView.as_view()), name='cadastrar-livro'),
    path('lista-livros', views.ListaLivrosView.as_view(), name='lista-livros'),
    path('livro/<int:pk>/', views.LivroDetalhadoView.as_view(), name='livro-detalhado'),
    path('adicionar_remover_favorito/<int:pk>/', login_required(views.AdicionarRemoverFavorito.as_view()), name='adicionar_remover_favorito'),
    path('livros_favoritos', login_required(views.LivrosFavoritosView.as_view()), name='livros_favoritos'),
    path('login/', auth_views.LoginView.as_view(template_name='management/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/', views.RegistrarView.as_view(template_name='management/registrar.html'), name='registrar'),
]
