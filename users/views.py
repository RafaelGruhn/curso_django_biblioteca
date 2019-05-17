from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.paginator import Paginator, InvalidPage

from .models import Usuario
from biblioteca.forms import UsuarioForm, EditUsuarioForm, LoginForm

# Create your views here.

def CadastroUsuario(request):
    if request.method == 'POST':
        #Cria o formulário com os dados preenchidos 
        formUsuario = UsuarioForm(request.POST)

        #Verifica se o formulário é válido
        if formUsuario.is_valid():
            user = Usuario
            user = formUsuario.save(commit=False)
            user.set_password(request.POST["password"])
            user.save()
            u = User.objects.create_user(username = user.username, password = request.POST["password"])
            u.save()
            print(user.password)
            return redirect("listarUsuarios")
        
        else:
            return render(request, 'usuarios/cadastroUsuario.html', {"form": UsuarioForm(request.POST)})

    else:
        context = {"form": UsuarioForm()}
        return render(request, 'usuarios/cadastroUsuario.html', context)


class ListarUsuarios(ListView):
    template_name = "usuarios/listarUsuarios.html"

    def get_queryset(self):
        return Usuario.objects.all()

    
def EditarUsuario(request, pk):

    if request.method == 'POST':
        #Cria o formulário com os dados preenchidos 
        formUsuario = EditUsuarioForm(request.POST)
        #Verifica se o formulário é válido
        if formUsuario.is_valid():
            usuario = Usuario()
            usuario = formUsuario.save(commit = False)
            usuario.pk = request.POST["pk"]
            usuario.set_password(request.POST["password"])
            print(usuario.pk)
            usuario.update()
            return redirect("listarUsuarios")
        
        return render(request, 'usuarios/editarUsuario.html', {"form": EditUsuarioForm(request.POST), 'pk': request.POST["pk"]})

    else:
        usuario = get_object_or_404(Usuario, pk = pk)
        context = {"form": EditUsuarioForm(instance = usuario), 'pk': pk}
        return render(request, 'usuarios/editarUsuario.html', context)


def ListarLivrosUsuario(request):
    ### Lista de livros locados pelo usuario atual
    user = get_object_or_404(Usuario, pḱ = request.user.pk)
    livros = user.livros_retirados.all().filter(status = False)
    page = request.GET.get("page", 1)
    paginator = Paginator(livros, 5)
    total = paginator.count
    try:
        livros2 = paginator.page(page)
    except Exception as e:
        print(e)
        livros2 = paginator.page(1)
    return render(request, "usuarios/usuario_livros.html", {"livros": livros2})


def Login(request):
    if request.user.id is not None:
        return redirect("home")
    
    elif request.method == 'POST':
        nome = request.POST['username']
        senha = request.POST['password']

        if nome and senha is not None:
            user = authenticate(username = nome, password = senha)

            if user is not None:
                login(request, user)
                return redirect('home')

            else:
                user = Usuario()
                user.username = nome
                return render(request, 'login.html', {'form': LoginForm(instance = user), 'mensagem': "Nome de usuário ou senha incorretos!"})
        else:
            user = Usuario()
            user.username = nome
            return render(request, 'login.html', {'form': LoginForm(instance = user), 'mensagem': "Nome de usuário ou senha estão em branco!"})

    else:
        return render(request, "login.html", {'form': LoginForm()})
