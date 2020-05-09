from django.db import models


class tipoPessoa(models.Model):
    tipo = models.CharField(max_length=12)

    def __str__(self):
        return self.tipo


class cargoPessoa(models.Model):
    cargo = models.CharField(max_length=64)

    def __str__(self):
        return self.cargo


class pessoa(models.Model):
    nome = models.CharField(max_length=120)
    telefone = models.CharField(max_length=15)
    matricula = models.CharField(max_length=16)
    tipo = models.ForeignKey(tipoPessoa, on_delete=models.PROTECT)
    cargo = models.ForeignKey(cargoPessoa, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.nome


class categoriaLivro(models.Model):
    categoria = models.CharField(max_length=120)

    def __str__(self):
        return self.nome


class livro(models.Model):
    nome = models.CharField(max_length=120)
    codigo = models.CharField(max_length=120)
    quantidade_total = models.IntegerField(null=True)
    data_hora_criacao = models.DateTimeField(auto_now_add=True)
    data_hora_alteracao = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(categoriaLivro, on_delete=models.PROTECT)
    pessoa = models.ForeignKey(pessoa, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.nome
