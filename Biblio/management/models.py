from django.db import models

# Create your models here.
class ModelLivro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='capas_livro/', null=True, blank=True)
    estoque = models.PositiveIntegerField(default=0)