from django.urls import path
from .views import *

app_name = "biblioteca"

urlpatterns = [
    path('listarPessoas', listarPessoas, name='listarPessoas'),
    path('listarLivros', listarLivros, name='listarLivros'),
    path('emprestimo', emprestimo, name='emprestimo'),
]
