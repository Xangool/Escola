from django.shortcuts import render
from .models import *


def listarPessoas(request):
    pessoas = Pessoa.objects.all()
    contexto = {
        "pessoas": pessoas,
    }

    return render(request, 'listarPessoas.html', contexto)


def listarLivros(request):
    livros = Livro.objects.all()

    contexto = {
        "todos_livros": livros,
    }

    return render(request, 'listarLivros.html', contexto)


def emprestimo(request):
    livros = Livro.objects.all()
    pessoa = Pessoa.objects.all()
    contexto = {
        "todos_livros": livros,
        "todas_pessoas": pessoa,
    }

    if (request.method == 'POST'):
        livroSelecionado = Livro.objects.get(id__exact=request.POST['livroSelecionado'])
        livroSelecionado.pessoa = Pessoa.objects.get(id__exact=request.POST['pessoaSelecionada'])
        livroSelecionado.save()

    return render(request, 'listarLivros.html', contexto)
