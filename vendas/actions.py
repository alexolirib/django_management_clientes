from django.http import HttpResponseNotFound
#método utilizado para admin

#criar as actions - fazer ações em algum elemento
def nef_emitida(modeladmin, request, queryset):
    if not request.user.has_perm('vendas.setar_nfe'):
        return HttpResponseNotFound('<h1>Sem permissão</h1>')
    queryset.update(nfe_emitida=True)

nef_emitida.short_description = "NFE Emitida"


def nfe_nao_emitida(modeladmin, request, queryset):
    if not request.user.has_perm('vendas.setar_nfe'):
        return HttpResponseNotFound('<h1>Sem permissão</h1>')
    queryset.update(nfe_emitida=False)


nfe_nao_emitida.short_description = "NFE não emitida"
