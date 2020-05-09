from warnings import catch_warnings

from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def listarPessoas(request):
    pessoas = Pessoa.objects.all()

    contexto = {
        "todas_pessoas": pessoas,
    }

    return render(request, 'listarpessoas.html', contexto)


def listarLivros(request):
    livros = Livro.objects.all()

    contexto = {
        "todos_livros": livros,
    }

    return render(request, 'listarlivros.html', contexto)


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

    return render(request, 'listarlivros.html', contexto)
