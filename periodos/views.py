from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.views import View

from periodos.forms import SearchPeriodo
from periodos.models import Periodo


class PeriodoListView(View):
    def get(self, request, *args, **kwargs):
        periodos = Periodo.objects.all().order_by('p_inicio')
        form = SearchPeriodo()
        context = {'periodos': periodos, 'form': form}

        pass
        return render(request, 'periodo/periodo_list.html', context)

    def post(self, request, *args, **kwargs):
        # return HttpResponseBadRequest("Request triste")
        form = SearchPeriodo(request.POST)

        if form.is_valid():
            i_periodo = form.data.get('dt_inicio')
            f_periodo = form.data.get('dt_fim')
            # query

            periodos = Periodo.filtrar_periodo_data_inicio(i_periodo, f_periodo)

            context = {'periodos': periodos, 'form': form}
            return render(request, 'periodo/periodo_list.html', context)

        periodos = Periodo.objects.all().order_by('p_inicio')

        context = {'periodos': periodos, 'form': form}
        return render(request, 'periodo/periodo_list.html', context)

class PeriodoDetailView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseBadRequest("Requisição triste")

