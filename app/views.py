from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.db import IntegrityError
from .models import Disciplina, Turma


def redirect_to_dashboard(request):
    return redirect('dashboard')


class LoginView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        error = request.session.pop('error', False)
        success = request.session.pop('success', False)
        warning = request.session.pop('warning', False)

        return render(request, 'auth/login.html', {'error': error, 'success': success, 'warning': warning})

    @staticmethod
    def post(request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('dashboard')
        else:
            request.session['error'] = 'Credenciais inválidas'
            return redirect('login')


class LogoutView(View):
    @staticmethod
    def post(request, *args, **kwargs):
        logout(request)

        request.session['warning'] = 'Você foi desconectado'
        return redirect('login')


class DashboardView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        error = request.session.pop('error', False)
        warning = request.session.pop('warning', False)
        success = request.session.pop('success', False)

        return render(request, 'dashboard/index.html', {'error': error,
                                                        'warning': warning,
                                                        'success': success})


class CriarTurmaView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        disciplinas = Disciplina.objects.all()

        error = request.session.pop('error', False)
        warning = request.session.pop('warning', False)
        success = request.session.pop('success', False)

        if len(disciplinas) == 0:
            error = 'Não existem disciplinas cadastradas, contate o administrador'

        return render(request, 'dashboard/criar_turma.html', {'error': error,
                                                              'warning': warning,
                                                              'success': success,
                                                              'disciplinas': disciplinas})

    @staticmethod
    def post(request, *args, **kwargs):
        try:
            t = Turma(nome=request.POST.get('nome').upper(),
                      disciplina=Disciplina.objects.get(id=int(request.POST.get('disciplina'))),
                      max_alunos=int(request.POST.get('max_alunos')),
                      professor=request.user)

            t.save()

            request.session['success'] = 'Turma criada com sucesso'
            return redirect('criar-turma')
        except IntegrityError:
            request.session['warning'] = 'Esta turma já existe'
            return redirect('criar-turma')
        except ValueError:
            request.session['warning'] = 'Valores inválidos'
            return redirect('criar-turma')


class RealizarMatriculaView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        turmas = Turma.objects.exclude(alunos_matriculados__id=request.user.id)

        error = request.session.pop('error', False)
        warning = request.session.pop('warning', False)
        success = request.session.pop('success', False)

        if len(turmas) == 0:
            error = 'Não existem turmas para matrícula, contate seu professor'

        return render(request, 'dashboard/realizar_matricula.html', {'error': error,
                                                                     'warning': warning,
                                                                     'success': success,
                                                                     'turmas': turmas})

    @staticmethod
    def post(request, *args, **kwargs):
        try:
            t = Turma.objects.get(id=int(request.POST.get('turma')))

            if t.alunos_matriculados.count() < t.max_alunos:
                t.alunos_matriculados.add(request.user)
                request.session['success'] = 'Matrícula realizada com sucesso'
                return redirect('realizar-matricula')
            else:
                request.session['warning'] = 'Número máximo de alunos atingidos'
                return redirect('realizar-matricula')

        except IntegrityError:
            request.session['warning'] = 'Ocorreu um erro na matrícula'
            return redirect('realizar-matricula')
        except ValueError:
            request.session['warning'] = 'Valores inválidos'
            return redirect('realizar-matricula')
