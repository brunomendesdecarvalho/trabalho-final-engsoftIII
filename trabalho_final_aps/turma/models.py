from django.db import models
from ..aluno.models import *
from ..professor.models import *


class Turma(models.Model):
    disciplina = models.CharField(max_length=25)
    alunos_matriculados = models.ManyToManyField(Aluno)