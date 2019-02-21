from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views import View

from client.models import Person


def home(request):
    return render(request, 'home.html')

def my_logout(request):
    logout(request)
    return redirect('tela_home')

class HomePageView(TemplateView):
    template_name = 'home3'

    def get_context_data(self, **kwargs):
        #recebendo o contexto do TemplateView
        context = super().get_context_data(**kwargs)
        context['minha_var'] = 'Olá tudo bem? Utilizando o HomePageView'
        return context

#views é baseada em functions
# FBV
#por classes
# CBV - built - in class-based views API

class MyView(View):
    def get(self, request, *args, **kwargs):
        #return HttpResponse('hello, world!')
        var = Person(first_name='Alxandre', last_name='Ribeiro')
        return render(request, 'home2.html',{'var': var})

    def post(self, request, *args, **kwargs ):
        return HttpResponse('Post')

class MyView2(View):
    def get(self, request, *args, **kwargs):
        #return HttpResponse('hello, world!')
        #breakpoint()
        # view2/<str:nome>/<int:id>
       # http: // localhost: 8000 / view2 / alex / 1
        # kwargs['id'] = 1
        # kwargs['nome'] = 1
        var = Person(first_name='Alxandre', last_name='Ribeiro')
        return render(request, 'home2.html',{'var': var})

    def post(self, request, *args, **kwargs ):
        return HttpResponse('Post')

