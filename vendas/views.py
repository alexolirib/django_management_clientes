from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import *
from .models import Venda, ItensDoPedido

class DashboardView(View):
    #Primeiros métodos que é disparado quando a view é chamada
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('vendas.ver_dashboard'):
            return HttpResponse('Acesso negado, voce precisa de permissão!')

        #retornar o caminho normal do meu dispatch
        return super(DashboardView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        #métodos estou pegando de vendas que está pegando do VendaManager
        media_venda = Venda.objects.media()
        media_desc_cabeçalho = Venda.objects.desconto_cabecalho()
        media_desc_por_produto = ItensDoPedido.objects.descoto_produto()
        qtd_vendas = Venda.objects.qtd_vendas()
        # nfe_impressa = len(Venda.objects.filter(nfe_emitida=True))
        #duas forma de fazer
        nfe_impressa = Venda.objects.nfe_impressa()
        min = Venda.objects.valor_min_venda()
        max = Venda.objects.valor_max_venda()

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

