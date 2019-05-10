from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth import authenticate, login

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
            
            user.save()
            print(user.password)
            return redirect("home")
        
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
        usuario = formUsuario.save(commit = False)
        #Verifica se o formulário é válido
        if usuario is not None:
            
            usuario.pk = request.POST["pk"]
            usuario.save()
            return redirect("listarUsuarios")
        
        return render(request, 'usuarios/editarUsuario.html', {"form": EditUsuarioForm(request.POST), 'pk': request.POST["pk"]})

    else:
        usuario = get_object_or_404(Usuario, pk = pk)
        context = {"form": EditUsuarioForm(instance = usuario), 'pk': pk}
        return render(request, 'usuarios/editarUsuario.html', context)


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
