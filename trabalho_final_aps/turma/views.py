from django.shortcuts import render, redirect
from professor.forms import ProfessorForm
from professor.models import Professor

# Create your views here.

def list_turmas(request):
    turmas = Turma.objects.all()
    return render(request, "list_turma.html", {'turmas': turmas})

def add_turma(request): # Apenas usuários professor e admin podem ativar essa função. Falta implementar essas condições.
    if request.method == "POST":
        form = TurmaForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_turmas')
    else:
        form = TurmaForm()
        return render(request, "add_turma.html", {'form': form})

