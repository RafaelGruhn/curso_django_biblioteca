from django.contrib import admin
from livros.models import Autor, Livro

class AdminLivro(admin.ModelAdmin):
    model = Livro
    list_display = ('titulo', 'editora', 'data', 'status')
    list_filter = ('editora',)

admin.site.register(Autor)
admin.site.register(Livro, AdminLivro)