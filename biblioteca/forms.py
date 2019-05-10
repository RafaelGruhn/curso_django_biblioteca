from django import forms

from users.models import Usuario
from livros.models import Livro

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        ##exclude = ('is_active', 'is_superuser', 'is_staff',)
        fields = ('username', 'password','first_name', 'last_name', 'email',)
        widgets = {
            'password': forms.PasswordInput,
            #'pk': forms.HiddenInput(),
        }


class EditUsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        ##exclude = ('is_active', 'is_superuser', 'is_staff',)
        fields = ('id', 'username', 'password','first_name', 'last_name', 'email',)
        widgets = {
            'password': forms.PasswordInput,
            #'pk': forms.HiddenInput(),
        }
    def __init__(self, *args, **kwargs):
        super(EditUsuarioForm, self).__init__(*args, **kwargs)
        self.fields['username'] = forms.CharField()


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ('__all__')


class LoginForm(forms.ModelForm):

    class Meta:
        model = Usuario
        ##exclude = ('is_active', 'is_superuser', 'is_staff',)
        fields = ('username', 'password',)
        widgets = {
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'] = forms.CharField()
