from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse

# Create your models here.

class Usuario(User):
    update_on = models.DateField("Atualizado em", auto_now_add = True, null = True)
    modify_on = models.DateField("Modificado em", auto_now = True, null = True)

    def get_absolute_url(self):
        return reverse("editarUsuario", kwargs={"pk": self.pk})
    