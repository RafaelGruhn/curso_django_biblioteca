<<<<<<< HEAD
from django.shortcuts import render, redirect
=======
from django.shortcuts import render
>>>>>>> origin/master

from biblioteca.forms import UsuarioForm

# Create your views here.

def CadastroUsuario(request):

    if request.method == 'POST':
        #Cria o formulário com os dados preenchidos 
        formUsuario = UsuarioForm(request.POST)

        #Verifica se o formulário é válido
        if formUsuario.is_valid():
            formUsuario.save()
<<<<<<< HEAD
            return redirect("home")
=======
            return render(request, "home.html", {})
>>>>>>> origin/master
        
        else:
            return render(request, 'cadastro.html', {"form": UsuarioForm(request.POST)})


    else:
        context = {"form": UsuarioForm()}
        return render(request, 'cadastro.html', context)
