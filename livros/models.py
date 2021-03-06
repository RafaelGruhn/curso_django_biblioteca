from django.db import models
import datetime
from django.urls import reverse
from django.contrib.auth.models import User

from users.models import Usuario
# Create your models here.

CHOICES_LIVRO_STATUS = (
    (False, "Indisponível"),
    (True, "Disponível"))


class Autor(models.Model):
    nome = models.CharField(max_length = 100, blank = False,
    null = False)
    email = models.EmailField()
    class Meta:
        verbose_name_plural = "Autores"
    def __str__(self):
        return self.nome + " - " + self.email            


class Livro(models.Model):
    titulo = models.CharField(max_length = 150, blank = False,
    null = False)
    editora = models.CharField(max_length = 100)
    data = models.DateField(null = False,
    default=datetime.date.today)
    status = models.BooleanField("Retirado: ",
    choices = CHOICES_LIVRO_STATUS)
    autor = models.ForeignKey(Autor, related_name = 'livros',
    on_delete = models.CASCADE)

    def __str__(self):
        return self.titulo

    def retirar_livro(self):
        if self.status == True:
            self.status = False
            return True
        return False

    def devolver_livro(self):
        if self.status == False:
            self.status = True
            return True
        return False

    def get_absolute_url(self):
        return reverse("home")
    