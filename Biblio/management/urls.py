from django.urls import path

from . import views

urlpatterns = [
    path('', views.PaginaInicialView.as_view(), name='index'),
    path('cadastrar', views.AdicionarLivroView.as_view(), name='cadastrar'),
]
