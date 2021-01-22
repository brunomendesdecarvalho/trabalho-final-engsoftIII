"""trabalho_final_aps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aluno import views as av
from professor import views as pv
from turma import views as tv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_aluno/', av.add_aluno, name='add_aluno'),
    path('list_alunos/', av.list_alunos, name='list_alunos'),
    path('add_professor/', pv.add_professor, name='add_professor'),
    path('list_professores/', pv.list_professores, name='list_professores'),
    path('add_turma/', tv.add_turma, name='add_turma'),
    path('list_turmas/', tv.list_turmas, name='list_turmas'),
]
