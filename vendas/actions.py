
#método utilizado para admin
#criar as actions - fazer ações em algum elemento
def nef_emitida(modeladmin, request, queryset):
    queryset.update(nfe_emitida=True)


nef_emitida.short_description = "NFE Emitida"


def nfe_nao_emitida(modeladmin, request, queryset):
    queryset.update(nef_emitida=False)


nfe_nao_emitida.short_description = "NFE não emitida"
