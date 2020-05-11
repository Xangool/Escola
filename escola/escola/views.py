from django.shortcuts import *
from .models import *


def cadastrarPessoa(requisicao):
    cargos = cargoPessoa.objects.all()
    tipos = tipoPessoa.objects.all()
    if requisicao.method == 'POST':
        tipoSelecionado = tipoPessoa.objects.get(id__exact=requisicao.POST['tipo'])
        pessoa_cadastro = pessoa(nome=requisicao.POST['nome'], telefone=requisicao.POST['telefone'],
                                 matricula=requisicao.POST['matricula'], tipo=tipoSelecionado)
        pessoa_cadastro.save()
    contexto = {
        'cargos': cargos,
        'tipos': tipos
    }
    return render(requisicao, 'Pessoa/cadastrarPessoa.html', contexto)


def cadastrarAluno(requisicao):
    if requisicao.method == 'POST':
        tipoSelecionado = tipoPessoa.objects.get(id__exact=1)
        pessoa_cadastro = pessoa(nome=requisicao.POST['nome'], telefone=requisicao.POST['telefone'],
                                 matricula=requisicao.POST['matricula'], tipo=tipoSelecionado)
        pessoa_cadastro.save()
    return render(requisicao, 'Aluno/cadastrarAluno.html')


def cadastrarFuncionario(requisicao):
    if requisicao.method == 'POST':
        sucesso = None
        if len(requisicao.POST['descricao']) > 0:
            cargoParaSalvar = cargoPessoa(descricao=requisicao.POST['descricao'])
            cargoParaSalvar.save()
            pessoa_cadastro = pessoa(nome=requisicao.POST['nome'], telefone=requisicao.POST['telefone'])
        else:
            tipoSelecionado = tipoPessoa.objects.get(id__exact=2)
            cargoSelecionado = cargoPessoa.objects.get(id__exact=requisicao.POST['cargo'])
            pessoa_cadastro = pessoa(nome=requisicao.POST['nome'], telefone=requisicao.POST['telefone'],
                                     tipo=tipoSelecionado,
                                     cargo=cargoSelecionado)
            pessoa_cadastro.save()
            pessoa_cadastro = pessoa()
            sucesso = "Funcionario cadastrado com sucesso"
        contexto = {
            'pessoa': pessoa_cadastro,
            'cargos': cargoPessoa.objects.all(),
            'sucesso': sucesso
        }
    else:
        cargos = cargoPessoa.objects.all()
        contexto = {
            'cargos': cargos,
        }
    return render(requisicao, 'Funcionario/cadastrarFuncionario.html', contexto)
