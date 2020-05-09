from django.shortcuts import render
from escola.escola.models import *
# Create your views here.

def listarPessoas(request):
    pessoas = pessoa.objects.all()
    contexto = {
        "pessoas": pessoas,
    }

    return render(request, 'listarPessoas.html', contexto)


def listarLivros(request):
    livros = livro.objects.all()

    contexto = {
        "todos_livros": livros,
    }

    return render(request, 'listarLivros.html', contexto)


def emprestimo(request):
    livros = livro.objects.all()
    pessoas = pessoa.objects.all()
    contexto = {
        "todos_livros": livros,
        "todas_pessoas": pessoas,
    }

    if (request.method == 'POST'):
        livroSelecionado = livro.objects.get(id__exact=request.POST['livroSelecionado'])
        livroSelecionado.pessoa = pessoa.objects.get(id__exact=request.POST['pessoaSelecionada'])
        livroSelecionado.save()

    return render(request, 'listarLivros.html', contexto)

def listarAlunos(request):
    alunos = pessoa.objects.all()
    contexto = {
        'alunos': alunos
    }
    return render(request, 'listarAlunos.html', contexto)


def cadastrarAluno(request):
    cadastro = aluno.objects.all()
    if (request.method == 'POST'):
        aluno = aluno(nome=request.POST['nome'], matricula=request.POST['matricula'])
        aluno.save()
    contexto = {
        'cadastro': cadastro,
    }
    return render(request, 'cadastrarAluno.html', contexto)