from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class Usuario(AbstractBaseUser):
    username = models.CharField("Nome de usuário", max_length=50)
    email = models.EmailField("E-mail", max_length=254)
    first_name = models.CharField("Primeiro nome", max_length=50)
    last_name = models.CharField("Último nome", max_length=50)
    update_on = models.DateField("Atualizado em", auto_now_add = True, null = True)
    modify_on = models.DateField("Modificado em", auto_now = True, null = True)

    USERNAME_FIELD = 'username'