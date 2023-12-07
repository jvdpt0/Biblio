from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class ModelUsuario(AbstractUser):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    foto_de_perfil = models.ImageField(upload_to='fotos_usuarios/', null=True, blank=True)

    def __str__(self):
        return self.username

class ModelLivro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='capas_livros/', null=True, blank=True)
    estoque = models.PositiveIntegerField(default=0)

    def media_nota(self):
        avaliacoes = ModelAnalise.objects.filter(livro=self)
        if avaliacoes.exists():
            return sum([analise.nota for analise in avaliacoes])/len(avaliacoes)
        return None

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

class ModelAnalise(models.Model):
    usuario = models.ForeignKey(ModelUsuario, on_delete=models.CASCADE)
    livro = models.ForeignKey(ModelLivro, on_delete=models.CASCADE, related_name='reviews')
    analise = models.TextField(null=True, blank=True)
    nota = models.IntegerField(default=0, choices=[(n,n) for n in range(6)])

    def __str__(self):
        return f"Analise feita por {self.usuario.username} para {self.livro.nome}"
    
    class Meta:
        verbose_name = 'Análise'
        verbose_name_plural = 'Análises'
    
class ModelFavoritos(models.Model):
    usuario = models.ForeignKey(ModelUsuario, on_delete=models.CASCADE)
    livro = models.ForeignKey(ModelLivro, on_delete=models.CASCADE)
    context_object_name = 'livros_favoritos'

    def __str__(self):
        return f"{self.livro.nome} Favorito de: {self.usuario.username}"
    
    class Meta:
        verbose_name = 'Favorito'
        verbose_name_plural = 'Favoritos'
    
class ModelAlugar(models.Model):
    usuario = models.ForeignKey(ModelUsuario, on_delete=models.CASCADE)
    livro = models.ForeignKey(ModelLivro, on_delete=models.CASCADE)
    data_solicitado = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return f"Livro {self.livro.nome} solicitado por {self.usuario.nome}"
    
    class Meta:
        verbose_name = 'Aluguel'
        verbose_name_plural = 'Alugueis'