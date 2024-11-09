from django import forms
from .models import User,Registro
from django.contrib.auth.forms import AuthenticationForm

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirme a senha")

    class Meta:
        model = User
        fields = ['email', 'password']

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password != password_confirm:
            raise forms.ValidationError("As senhas não coincidem")
        return password_confirm
    def save(self, commit=True):
        # Sobrescreve o método save para definir a senha corretamente
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Senha"}))
    

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = [
            'id_porteiro', 'id_condominio', 'nome_condominio', 'nome_cadastro',
            'nome_completo', 'cargo', 'cpf', 'telefone', 'nome_usuario',
            'senha_usuario', 'img_funcionario', 'status_acesso', 'cliente', 'grupo', 'whastapp'
        ]
        widgets = {
            'senha_usuario': forms.PasswordInput(),
        }