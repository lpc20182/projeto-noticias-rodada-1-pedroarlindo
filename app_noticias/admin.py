from django.contrib import admin
from .models import *


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    pass

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    pass


@admin.register(MensagemDeContato)
class MensagemDeContatoAdmin(admin.ModelAdmin):
    readonly_fields = ('data',)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}
