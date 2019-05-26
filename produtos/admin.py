from django.contrib import admin
from produtos.models import Produto



class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'preco')
    search_fields = ['id', 'descricao']


admin.site.register(Produto, ProdutoAdmin)
