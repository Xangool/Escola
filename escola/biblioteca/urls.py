from django.urls import path
from .views import *

app_name = "biblioteca"

urlpatterns = [
    path('listarpessoas',listarPessoas,name='todas_pessoas'),
    path('listarlivros',listarLivros,name='todos_livros'),
    path('emprestimo', emprestimo,name='emprestimo'),
]
