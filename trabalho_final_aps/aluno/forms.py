from django.forms import ModelForm
from .models import *


class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'