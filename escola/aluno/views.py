from django.shortcuts import render
from .models import *


def listarAlunos(request):
    alunos = Aluno.objects.all()
    contexto = {
        'alunos':alunos
    }
    return render(request, 'listarAlunos.html', contexto)


def cadastrarAluno(request):
    cadastro = Aluno.objects.all()
    if (request.method == 'POST'):
        aluno = Aluno(nome=request.POST['nome'])
        aluno.save()
    contexto = {
        'cadastro': cadastro,
    }
    return render(request, 'cadastrarAluno.html', contexto)
