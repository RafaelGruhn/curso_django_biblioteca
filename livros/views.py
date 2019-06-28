from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, InvalidPage
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from livros import models
from biblioteca.forms import LivroForm
from users.models import Usuario

# Create your views here.
@login_required
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


class CadastroLivro(CreateView):

    model = models.Livro
    form_class = LivroForm
    template_name = "livros/cadastroLivro.html"
    success_url = "../../home/"

""" if request.method == "POST":
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
"""


class  EditarLivro(UpdateView):
    model = models.Livro
    form_class = LivroForm
    template_name = "livros/editarLivro.html"
    success_url = "../../home/"


class ExcluirLivro(DeleteView):
    model = models.Livro
    success_url = reverse_lazy("home")
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


@login_required
def ReservarLivro(request, pk):
    livro = get_object_or_404(models.Livro, pk=pk)
    if livro.retirar_livro():
        livro.usuario = request.user
        livro.status = False
        livro.save()
        ### Lista de livros locados pelo usuario atual
        return redirect("lista_livros_usuario")
    return redirect("home")

@login_required
def DevolverLivro(request, pk):
    livro = get_object_or_404(models.Livro, pk=pk)
    if livro.usuario == request.user:
        if livro.devolver_livro():
            livro.user = None
            livro.save()
            return redirect("lista_livros_usuario")
    return redirect("home")




















