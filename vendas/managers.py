from django.db import models
from django.db.models import Avg, Count, Min, Max


class VendaManager(models.Manager):
    def media(self):
        return self.all().aggregate(media=Avg('valor'))['media']

    def desconto_cabecalho(self):
        return self.all().aggregate(desc=Avg('desconto'))['desc']

    def qtd_vendas(self):
        return self.all().aggregate(qtd_prod=Count('id'))['qtd_prod']

    def nfe_impressa(self):
        return self.filter(nfe_emitida=True).aggregate(Count('id'))['id__count']

    def valor_max_venda(self):
        return self.all().aggregate(Max('valor'))['valor__max']

    def valor_min_venda(self):
        return self.all().aggregate(valor_min=Min('valor'))['valor_min']


class ItensDoPedidoManager(models.Manager):

    def descoto_produto(self):
        return self.all().aggregate(media_desc_prod=Avg("desconto"))['media_desc_prod']
