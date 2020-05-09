from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(tipoPessoa)
admin.site.register(cargoPessoa)
admin.site.register(pessoa)
admin.site.register(categoriaLivro)
admin.site.register(livro)