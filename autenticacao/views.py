from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegistrationForm, UserLoginForm, RegistroForm, Registro  # Certifique-se de que está importando UserLoginForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages


def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserRegistrationForm()
    return render(request, "autenticacao/register.html", {"form": form})
def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')  # Ajuste conforme necessário
    else:
        form = RegistroForm()
    
    return render(request, 'autenticacao/registro.html', {'form': form})
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu usuário',
            'id': 'id_username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha',
            'id': 'id_password'
        })
    )
class UserLoginView(LoginView):
    template_name = "autenticacao/login.html"
    form_class = UserLoginForm

    def form_invalid(self, form):
        messages.error(self.request, 'Usuário ou senha inválidos.')
        return super().form_invalid(form)
@login_required
def dashboard_view(request):
    # Lógica para exibir informações e atividades no dashboard
    return render(request, 'autenticacao/dashboard.html')
def gerenciamento_placeholder(request):
    return render(request, 'autenticacao/placeholder.html', {'feature_name': 'Painel de Controle'})

def gerenciar_usuarios(request):
    funcionarios = Registro.objects.all()
    return render(request, 'autenticacao/gerenciar_usuarios.html', {'funcionarios': funcionarios})

def residencia_placeholder(request):
    return render(request, 'autenticacao/placeholder.html', {'feature_name': 'Filtros por Residência'})

def residencias_placeholder(request):
    return render(request, 'autenticacao/placeholder.html', {'feature_name': 'Vinculação de Residências'})

def historico_placeholder(request):
    return render(request, 'autenticacao/placeholder.html', {'feature_name': 'Histórico de Mudanças'})

def encomenda_placeholder(request):
    return render(request, 'autenticacao/placeholder.html', {'feature_name': 'Consulta de Encomenda'})

def inquilinos_placeholder(request):
    return render(request, 'autenticacao/placeholder.html', {'feature_name': 'Controle de Inquilinos'})

def acesso_placeholder(request):
    return render(request, 'autenticacao/placeholder.html', {'feature_name': 'Controle de Acesso e Permissões'})
def editar_funcionario(request, id_porteiro):
    # View temporária
    return render(f"Página de edição do funcionário {id_porteiro}")

def deletar_funcionario(request, id_porteiro):
    # View temporária
    return render(f"Página de exclusão do funcionário {id_porteiro}")