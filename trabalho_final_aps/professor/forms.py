from django.forms import ModelForm
from .models import *


class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'