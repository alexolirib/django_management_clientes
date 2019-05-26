from django.contrib import admin
from vendas.actions import nef_emitida, nfe_nao_emitida
from vendas.models import Venda, ItensDoPedido

#forma para inserir vários ao mesmo tempo
#admin.TabularInline
#admin.stackInline
class ItemPedidoInline(admin.TabularInline):
    model = ItensDoPedido
    extra = 1


# para registrar meus models e ficar visível na aplicação

# filtrar as vendas de pessoas com os cpf
class VendaAdmin(admin.ModelAdmin):
    actions = [nef_emitida, nfe_nao_emitida]
    # forma que funciona na versão do django antigo
    # raw_id_fields = ('person',)
    # é preciso implementar na classe PersonAdmin(search_fields)
    # autocomplete_fields = ('person','produtos')
    autocomplete_fields = ('person',)
    readonly_fields = ('valor',)
    fieldsets = (
        ('Dados da venda', {'fields': (('numero',),)}),
        ('Dados da venda', {'fields': (('desconto', 'imposto'),)}),
        ('Dados complementares', {
            'fields': ('person', ('nfe_emitida',),
                       'valor')
        })
    )
    # list_display = ('get_doc_person', 'desconto', 'person',
    #                 'total_bruto', 'taxas_e_desconto', 'total_liquido', 'nfe_emitida')
    list_display = ('get_doc_person', 'desconto', 'person',
                    'nfe_emitida')
    inlines = [ItemPedidoInline]

    # forma das versões antigas
    # filter_horizontal = ['produtos', ]

    # def taxas_e_desconto(self, obj):
    #     total = self.total_bruto(obj) - self.total_liquido(obj)
    #     return str(f'{total} ({(total / self.total_bruto(obj)) * 100}%)')
    #
    # def total_bruto(self, obj):
    #     return obj.value_all_sale()
    #
    # def total_liquido(self, obj):
    #     return obj.get_total()

    def get_doc_person(self, obj):
        return obj.person.doc

    get_doc_person.short_description = 'Documento da Pessoa'


admin.site.register(ItensDoPedido)
admin.site.register(Venda, VendaAdmin)
