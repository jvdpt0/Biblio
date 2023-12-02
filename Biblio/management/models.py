from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class ModelUsuario(AbstractUser):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    foto_de_perfil = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)

    def __str__(self):
        return self.username

class ModelLivro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='capas_livro/', null=True, blank=True)
    estoque = models.PositiveIntegerField(default=0)

    def media_nota(self):
        avaliações = ModelAnalise.objects.filter(livro=self)
        if avaliações.exists():
            return sum([analise.nota for analise in avaliações])
        return None

    def __str__(self):
        return self.nome

class ModelAnalise(models.Model):
    usuario = models.ForeignKey(ModelUsuario, on_delete=models.CASCADE)
    livro = models.ForeignKey(ModelLivro, on_delete=models.CASCADE, related_name='reviews')
    analise = models.TextField(null=True, blank=True)
    nota = models.IntegerField(default=0, choices=[(n,n) for n in range(6)])

    def __str__(self):
        return f"Analise feita por {self.usuario.username} para {self.livro.nome}"