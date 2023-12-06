from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.PaginaInicialView.as_view(), name='index'),
    path('cadastrar-livro', views.AdicionarLivroView.as_view(), name='cadastrar-livro'),
    path('lista-livros', views.ListaLivrosView.as_view(), name='lista-livros'),
    path('login/', auth_views.LoginView.as_view(template_name='management/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/', views.RegistrarView.as_view(template_name='management/registrar.html'), name='registrar'),
    path('livros_favoritos', views.LivrosFavoritos.as_view(), name='livros_favoritos'),
]
