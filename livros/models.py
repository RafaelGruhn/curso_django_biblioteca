from django.db import models
import datetime
# Create your models here.

class Autor(models.Model):
    nome = models.CharField(max_length = 100, blank = False, null = False)
    email = models.EmailField()
    class Meta:
        verbose_name_plural = "Autores"
    def __str__(self):
        return self.nome + " - " + self.email            


class Livro(models.Model):
    titulo = models.CharField(max_length = 150, blank = False, null = False)
    editora = models.CharField(max_length = 100)
    data = models.DateField(null = False, default=datetime.date.today)
    autor = models.ForeignKey(Autor, related_name = 'livros',on_delete = models.PROTECT)
    
    def __str__(self):
        return self.titulo
