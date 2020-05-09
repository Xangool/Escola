from django.urls import path
from escola.escola.views import *

app_name = "escola"

urlpatterns = [
    path("listarAlunos", listarAlunos, name="listarAlunos"),
    path("cadastrarAluno", cadastrarAluno, name="cadastrarAluno"),
    path('listarPessoas', listarPessoas, name='listarPessoas'),
    path('listarLivros', listarLivros, name='listarLivros'),
    path('emprestimo', emprestimo, name='emprestimo'),
]
