from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, InvalidPage

from livros import models

from biblioteca.forms import LivroForm
from users.models import Usuario

# Create your views here.

def home(request):
    livros = models.Livro.objects.all()
    page = request.GET.get("page", 1)
    paginator = Paginator(livros, 5)
    total = paginator.count
    try:
        livros2 = paginator.page(page)
    except Exception as e:
        livros2 = paginator.page(1)
    return render(request, "home.html", {"livros": livros2})


def CadastroLivro(request):
    if request.method == "POST":
        #Cria o formulário com os dados preenchidos 
        formLivro = LivroForm(request.POST)

        #Verifica se o formulário é válido
        if formLivro.is_valid():
            formLivro.save()
            return redirect("home")
        
        else:
            return render(request, 'livros/cadastroLivro.html', {"form": LivroForm(request.POST)})

    else:
        return render(request, "livros/cadastroLivro.html", {'form': LivroForm()})


def EditarLivro(request, pk):
    if request.method == "POST":
        #Cria o formulário com os dados preenchidos 
        formLivro = LivroForm(request.POST)

        #Verifica se o formulário é válido
        if formLivro.is_valid():
            livro = models.Livro
            livro = formLivro.save(commit = False)
            livro.pk = request.POST['pk']
            livro.save()
            return redirect("home")
        
        else:
            return render(request, 'livros/editarLivro.html', {"form": LivroForm(request.POST)})

    else:
        #livros = models.Livro.objects.all().filter(pk = pk)
        #for l in livros:
        #    livro = l
        livro = get_object_or_404(models.Livro, pk=pk)
        return render(request, "livros/editarLivro.html", {'form': LivroForm(instance = livro), 'pk': livro.pk})

def ExcluirLivro(request, pk):
    livro = get_object_or_404(models.Livro, pk=pk)
    livro.delete()
    return redirect("home")


def ReservarLivro(request, pk):
    livro = get_object_or_404(models.Livro, pk=pk)
    user = get_object_or_404(Usuario, pk=request.user.pk)
    if livro.retirar_livro():
        livro.usuario = user
        livro.status = False
        livro.save()
        ### Lista de livros locados pelo usuario atual
        return redirect("lista_livros_usuario")
    return redirect("home")


def DevolverLivro(request, pk):
    livro = get_object_or_404(models.Livro, pk=pk)
    user = get_object_or_404(Usuario, pk=request.user.pk)
    if livro.usuario == user:
        if livro.devolver_livro():
            livro.usuario = None
            livro.save()
            return redirect("lista_livros_usuario")
    return redirect("home")



        




















