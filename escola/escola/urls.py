from django.urls import path
from escola.escola.views import *

app_name = "escola"

urlpatterns = [
    path("cadastrarAluno", cadastrarAluno, name="cadastrarAluno"),
    path('cadastrarPessoa', cadastrarPessoa, name='cadastrarPessoa'),
    path('cadastrarFuncionario', cadastrarFuncionario, name='cadastrarFuncionario'),
    path('cadastrarCargo', cadastrarCargo, name='cadastrarCargo'),
]
