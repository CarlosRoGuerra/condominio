from django.urls import path
from .views import register_view, UserLoginView, dashboard_view
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("dashboard/", dashboard_view, name="dashboard"),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboard/gerenciamento/', views.gerenciamento_placeholder, name='dashboard_gerenciamento'),
    path('dashboard/filtros_residencia/', views.residencia_placeholder, name='filtros_residencia'),
    path('dashboard/vincular_residencias/', views.residencias_placeholder, name='vincular_residencias'),
    path('dashboard/historico_mudancas/', views.historico_placeholder, name='historico_mudancas'),
    path('dashboard/consulta_encomenda/', views.encomenda_placeholder, name='consulta_encomenda'),
    path('dashboard/controle_inquilinos/', views.inquilinos_placeholder, name='controle_inquilinos'),
    path('dashboard/controle_acesso/', views.acesso_placeholder, name='controle_acesso'),
    path("register/", register_view, name="register"),
    path('registro/', views.registro_view, name='registro'),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('dashboard/gerenciar_usuarios/', views.gerenciar_usuarios, name='gerenciar_usuarios'),
    path('dashboard/gerenciar_usuarios/adicionar/', views.registro_view, name='adicionar_funcionario'),
    path('dashboard/gerenciar_usuarios/editar/<int:id_porteiro>/', views.registro_view, name='editar_funcionario'),
    path('dashboard/gerenciar_usuarios/deletar/<int:id_porteiro>/', views.registro_view, name='deletar_funcionario'),
]