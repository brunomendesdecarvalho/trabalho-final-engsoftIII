from django.db import models
from ..turma.models import *

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length = 10)
    turmas_matriculadas = models.ManyToManyField(Turma)