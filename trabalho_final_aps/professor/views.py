from django.shortcuts import render, redirect
from professor.forms import ProfessorForm
from professor.models import Professor

# Create your views here.

def list_professores(request):
    professores = Professor.objects.all()
    return render(request, "list_professor.html", {'professores': professores})

def add_professor(request): # Só admin deve poder fazer isso. Falta implementar.
    if request.method == "POST":
        form = ProfessorForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_professores')
    else:
        form = ProfessorForm()
        return render(request, "add_professor.html", {'form': form})
