from django.shortcuts import *
from .models import *


# Create your views here.

# def listarPessoas(request):
#     pessoas = pessoa.objects.all()
#     contexto = {
#         "pessoas": pessoas,
#     }
#
#     return render(request, 'listarPessoas.html', contexto)
#
#
# def listarLivros(request):
#     livros = livro.objects.all()
#
#     contexto = {
#         "todos_livros": livros,
#     }
#
#     return render(request, 'listarLivros.html', contexto)
#
#
# def emprestimo(request):
#     livros = livro.objects.all()
#     pessoas = pessoa.objects.all()
#     contexto = {
#         "todos_livros": livros,
#         "todas_pessoas": pessoas,
#     }
#
#     if (request.method == 'POST'):
#         livroSelecionado = livro.objects.get(id__exact=request.POST['livroSelecionado'])
#         livroSelecionado.pessoa = pessoa.objects.get(id__exact=request.POST['pessoaSelecionada'])
#         livroSelecionado.save()
#
#     return render(request, 'listarLivros.html', contexto)
#
# def listarAlunos(request):
#     alunos = pessoa.objects.all()
#     contexto = {
#         'alunos': alunos
#     }
#     return render(request, 'listarAlunos.html', contexto)
#
#
# def cadastrarAluno(request):tipo
#     cadastro = aluno.objects.all()
#     if (request.method == 'POST'):
#         aluno = aluno(nome=request.POST['nome'], matricula=request.POST['matricula'])
#         aluno.save()
#     contexto = {
#         'cadastro': cadastro,
#     }
#     return render(request, 'cadastrarAluno.html', contexto)

def cadastrarPessoa(requisicao):
    cargos = cargoPessoa.objects.all()
    tipos = tipoPessoa.objects.all()
    if (requisicao.method == 'POST'):
        tipoSelecionado = tipoPessoa.objects.get(id__exact=requisicao.POST['tipo'])
        pessoa_cadastro = pessoa(nome=requisicao.POST['nome'], telefone=requisicao.POST['telefone'],
                                 matricula=requisicao.POST['matricula'], tipo=tipoSelecionado)
        pessoa_cadastro.save()
    contexto = {
        'cargos': cargos,
        'tipos': tipos
    }
    return render(requisicao, 'cadastrarPessoa.html', contexto)


def cadastrarAluno(requisicao):
    if (requisicao.method == 'POST'):
        tipoSelecionado = tipoPessoa.objects.get(id__exact=1)
        pessoa_cadastro = pessoa(nome=requisicao.POST['nome'], telefone=requisicao.POST['telefone'],
                                 matricula=requisicao.POST['matricula'], tipo=tipoSelecionado)
        pessoa_cadastro.save()
    return render(requisicao, 'cadastrarAluno.html')


def cadastrarFuncionario(requisicao):
    cargos = cargoPessoa.objects.all()
    if (requisicao.method == 'POST'):
        tipoSelecionado = tipoPessoa.objects.get(id__exact=1)
        cargoSelecionado = cargoPessoa.objects.get(id__exact=requisicao.POST['cargo'])
        pessoa_cadastro = pessoa(nome=requisicao.POST['nome'], telefone=requisicao.POST['telefone'],
                                 matricula=requisicao.POST['matricula'], tipo=tipoSelecionado, cargo=cargoSelecionado)
        pessoa_cadastro.save()
    contexto = {
        'cargos': cargos,
    }
    return render(requisicao, 'cadastrarFuncionario.html', contexto)


def cadastrarCargo(requisicao):
    cargos = cargoPessoa.objects.all()
    if (requisicao.method == 'POST'):
        cargoCadastro = cargoPessoa(descricao=requisicao.POST['descricao'])
        cargoCadastro.save()
    contexto = {
        'cargos': cargos,
    }
    return render(requisicao, 'cadastrarFuncionario.html', contexto)