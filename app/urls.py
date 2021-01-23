from django.urls import path
from .views import DashboardView, redirect_to_dashboard, LoginView, LogoutView, CriarTurmaView, RealizarMatriculaView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),

    path('dashboard/', login_required(DashboardView.as_view(), login_url='login'), name='dashboard'),
    path('dashboard/criar-turma/', login_required(CriarTurmaView.as_view(), login_url='login'), name='criar-turma'),
    path('dashboard/realizar-matricula/', login_required(RealizarMatriculaView.as_view(), login_url='login'),
         name='realizar-matricula'),

    path('', redirect_to_dashboard),
]
