from django.contrib import admin

from .models import ModelUsuario, ModelLivro, ModelAnalise, ModelFavoritos, ModelAlugar

# Register your models here.
admin.site.register(ModelUsuario)
admin.site.register(ModelLivro)
admin.site.register(ModelAnalise)
admin.site.register(ModelFavoritos)
admin.site.register(ModelAlugar)