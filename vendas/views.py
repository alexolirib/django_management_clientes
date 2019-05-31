from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import *
from .models import Venda

class DashboardView(View):
    def get(self, request):
        media = Venda.objects.all().aggregate(media=Avg('valor'))['media']
        context = {'media': media}
        return render(request, 'vendas/dashboard.html', context)

