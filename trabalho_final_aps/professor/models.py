from django.db import models
from aluno.models import *


class Professor(models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=10)