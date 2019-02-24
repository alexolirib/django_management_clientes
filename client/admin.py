from django.contrib import admin

from client.models import Person, Document, Venda, Produto, Periodo

# para registrar meus models e ficar visível na aplicação

admin.site.register(Person)
admin.site.register(Document)
admin.site.register(Venda)
admin.site.register(Produto)
admin.site.register(Periodo)

