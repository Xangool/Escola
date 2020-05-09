from django.forms import Form
from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def listarAlunos (request):
    alunos = Aluno.objects.all()

    contexto = {
        "todos_alunos" : alunos
    }

    return render(request,'listar.html', contexto)

def Cadastrar (request):
    cadastro = Aluno.objects.all()
    if (request.method == 'POST'):
        # import pdb
        # pdb.set_trace()
        aluno = Aluno(nome=request.POST['your_name'])
        aluno.save()
    contexto = {
        'cadastro': cadastro,
    }
    return render(request, 'cadastro.html', contexto)

# django com crispy forms
#