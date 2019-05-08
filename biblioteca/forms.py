from django import forms

from users.models import Usuario
from livros.models import Livro

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        ##exclude = ('is_active', 'is_superuser', 'is_staff',)
        fields = ('username', 'password','first_name', 'last_name', 'email',)

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ('__all__')