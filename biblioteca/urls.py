"""biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin

from livros.views import home, CadastroLivro, EditarLivro, ExcluirLivro, ReservarLivro, DevolverLivro
from users.views import CadastroUsuario, ListarUsuarios, EditarUsuario, Login, ListarLivrosUsuario


urlpatterns = [
    path('', Login, name = 'login'),
    path('home/', home, name='home'),
    path('users/cadastro_usuario/', CadastroUsuario, name='cadastroUsuario'),
    path('users/listar_usuarios/', ListarUsuarios.as_view(), name='listarUsuarios'),
    path('users/<int:pk>/editar_usuario/', EditarUsuario.as_view(), name='editarUsuario'),
    path('users/devolver_livro/', DevolverLivro, name='devolverLivro'),
    path('users/listar_livros/', ListarLivrosUsuario, name='lista_livros_usuario'),
    path('livros/cadastro_livro/', CadastroLivro.as_view(), name='cadastroLivro'),
    path('livros/<int:pk>/editar_livro/', EditarLivro, name='editarLivro'),
    path('livros/<int:pk>/excluir/',ExcluirLivro, name='excluirLivro'),
    path('livros/<int:pk>/reservar_livro/', ReservarLivro, name='reservarLivro'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'))
]
