from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("O email é obrigatório")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
class Registro(models.Model):
    id_porteiro = models.AutoField(primary_key=True)
    id_condominio = models.IntegerField()
    nome_condominio = models.CharField(max_length=255)
    nome_cadastro = models.CharField(max_length=255)
    nome_completo = models.CharField(max_length=255)
    cargo = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15)
    nome_usuario = models.CharField(max_length=150, unique=True)
    senha_usuario = models.CharField(max_length=255)
    img_funcionario = models.ImageField(upload_to='funcionarios/', null=True, blank=True)
    data = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    img_cod = models.CharField(max_length=255, null=True, blank=True)
    status_acesso = models.CharField(max_length=100)
    cliente = models.CharField(max_length=100)
    grupo = models.CharField(max_length=100)
    whastapp = models.CharField(max_length=15, null=True, blank=True)
    class Meta:
        db_table = 'funcionarios'
        managed = False  # Adicione esta linha se a tabela já existe no banco de dados

