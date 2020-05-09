from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=120)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=120)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    nome = models.CharField(max_length=120)
    codigo = models.CharField(max_length=120)
    quantidade_total = models.IntegerField(null=True)
    data_hora_criacao = models.DateTimeField(auto_now_add=True)
    data_hora_alteracao = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.nome


class Aluno (models.Model):
    nome = models.CharField(max_length=32)
    matricula = models.CharField(max_length=16)

    def __str__(self):
        return self.nome