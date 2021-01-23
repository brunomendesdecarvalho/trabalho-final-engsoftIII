from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    estudante = models.BooleanField(default=False)
    professor = models.BooleanField(default=False)


class Disciplina(models.Model):
    nome = models.CharField(max_length=255)
    carga_horaria = models.IntegerField()


class Turma(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    max_alunos = models.IntegerField()
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    professor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='professor_da_turma')
    alunos_matriculados = models.ManyToManyField(User, related_name='alunos_matriculados')

