from django.contrib import admin

from client.models import Person, Document, Venda, Produto, Periodo

#personalizar admin
class PersonAdmin(admin.ModelAdmin):
    #fields e fieldsets = para formulario
    # fields = (('first_name','last_name' ),('age', 'salary'), 'bio', 'photo', 'doc')
    fieldsets= (
        ('Dados pessoais', {'fields': (('first_name', 'last_name'),)}),
        ('Dados complementares', {
            'classes': ('collapse',),
            'fields': (('age', 'salary'), 'bio', 'photo', 'doc')
        })
    )

    list_display = ('first_name', 'last_name'  ,'age', 'salary', 'bio', 'has_photo', 'doc')

    def has_photo(self, obj):
        if obj.photo:
            return "SIM"
        return "NÃo"
    has_photo.short_description = 'Possui foto'

    # fazer filtro
    list_filter = ('age', 'salary')

# para registrar meus models e ficar visível na aplicação

#filtrar as vendas de pessoas com os cpf
class VendaAdmin(admin.ModelAdmin):
    readonly_fields = ('valor',)
    fieldsets = (
        ('Dados da venda', {'fields': (('numero',),)}),
        ('Dados da venda', {'fields': (('desconto', 'imposto'),)}),
        ('Dados complementares', {
            'fields': ('person', 'produtos')
        })
    )
    list_display = ('get_doc_person', 'desconto', 'person',
                    'total_bruto', 'taxas_e_desconto', 'total_liquido')

    def taxas_e_desconto(self, obj):
        total = self.total_bruto(obj) - self.total_liquido(obj)
        return str(f'{total} ({(total/self.total_bruto(obj))*100}%)')

    def get_doc_person(self, obj):
        return obj.person.doc

    def total_bruto(self, obj):
        return obj.value_all_sale()

    def total_liquido(self, obj):
        return obj.get_total()

    get_doc_person.short_description = 'Documento da Pessoa'



class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'preco')


admin.site.register(Person, PersonAdmin)
admin.site.register(Document)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Periodo)

