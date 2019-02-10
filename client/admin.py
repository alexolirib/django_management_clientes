from django.contrib import admin

from client.models import Person
# para registrar meus models e ficar visível na aplicação

admin.site.register(Person)

