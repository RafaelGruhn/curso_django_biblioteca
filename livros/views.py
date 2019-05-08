from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage

from livros import models

from biblioteca.forms import LivroForm

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
            return home(request)
        
        else:
            return render(request, 'cadastro.html', {"form": LivroForm(request.POST)})


    else:
        return render(request, "cadastroLivros.html", {'form': LivroForm()})
