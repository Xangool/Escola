from django.urls import path
from .views import *

app_name = "aluno"

urlpatterns = [
    path("listar",listarAlunos,name="todos_alunos"),
    path("cadastrar",Cadastrar,name="cadastro"),
]
