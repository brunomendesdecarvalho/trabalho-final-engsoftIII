from django.shortcuts import render, redirect
from aluno.forms import AlunoForm
from aluno.models import Aluno

# Create your views here.

def list_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, "list_aluno.html", {'alunos': alunos})

def add_aluno(request): # Só admin deve poder fazer isso. Falta implementar.
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_alunos')
    else:
        form = AlunoForm()
        return render(request, "add_aluno.html", {'form': form})
