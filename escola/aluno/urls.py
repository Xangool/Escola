from django.urls import path
from .views import *

app_name = "aluno"

urlpatterns = [
    path("listarAlunos", listarAlunos, name="listarAlunos"),
    path("cadastrarAluno", cadastrarAluno, name="cadastrarAluno"),
]
