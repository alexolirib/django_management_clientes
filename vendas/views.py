from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import *
from .models import Venda, ItensDoPedido

class DashboardView(View):
    def get(self, request):
        media_venda = Venda.objects.all().aggregate(media=Avg('valor'))['media']
        media_desc_cabeçalho = Venda.objects.all().aggregate(desc= Avg('desconto'))['desc']
        media_desc_por_produto = ItensDoPedido.objects.all().aggregate(media_desc_prod=Avg("desconto"))['media_desc_prod']
        qtd_vendas = len(Venda.objects.all())
        # nfe_impressa = len(Venda.objects.filter(nfe_emitida=True))
        #duas forma de fazer
        nfe_impressa = Venda.objects.filter(
            nfe_emitida=True).aggregate(Count('id'))['id__count']
        min = Venda.objects.all().aggregate(valor_min = Min('valor'))['valor_min']
        max = Venda.objects.all().aggregate(Max('valor'))['valor__max']
        context = {'media': media_venda,
                   'media_desc_cabecalho': media_desc_cabeçalho,
                   'media_desc_por_produto': media_desc_por_produto,
                   'desconto_total': (media_desc_cabeçalho+media_desc_por_produto)/2,
                   'qtd_vendas': qtd_vendas,
                   'nfe_impressa': nfe_impressa,
                   'venda_max': max,
                   'venda_min': min
                   }
        return render(request, 'vendas/dashboard.html', context)

