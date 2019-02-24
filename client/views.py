from django.utils import timezone
from django.http import HttpResponse, HttpResponseBadRequest, Http404, HttpResponseNotFound

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View

from client.forms import PersonForm, SearchPeriodo
from client.models import Person, Periodo
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#ele descubra a url de acordo com o nome
from django.urls import reverse_lazy
from django.db.models import Q

#@login_required - para poder ter acesso a essa minha view somente cquem está
#autenticado na aplicação

@login_required
def persons_list(request):
    #lista todos os clientes
    persons = Person.objects.all()
    return render(request, 'person.html', {'v_persons': persons, 'footer_args': 'Tela list'})

@login_required
def persons_new(request):
    #verifica se já tem algo, se não envia vazio
    #request.FILES - arquivos de midias que estão sendo enviados
    form = PersonForm(request.POST or None,request.FILES or None)
    breakpoint()

    if form.is_valid():
        form.save()
        return redirect(persons_list)
    return render(request, 'person_form.html', {'form': form})

@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect(persons_list)
    return render(request, 'person_form.html', {'form': form})



@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person,  pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if request.method == 'POST':
        person.delete()
        return redirect(persons_list)
    return render(request, 'person_delete_confirm.html', {'person': person, 'form':form})

#se não informar o template_name ele pega o padrão (está em pasta de client)
class PersonList(ListView):
    model = Person
    #definir um template para exibir
    #template_name = 'home3.html'

class PersonDetail(DetailView):
    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class PersonCreate(CreateView):
    model = Person
    #personalizar os fields
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']

    success_url = '/client/person_list'

class PersonUpdate(UpdateView):
    model = Person
    #personalizar os fields
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = reverse_lazy('person_list_cbv')

class PersonDelete(DeleteView):
    model = Person
    #success_url = reverse_lazy('person_list_cbv')
    #outra forma que ficar melhor para manipular
    def get_success_url(self):
        #consigo manipular melhor
        return reverse_lazy('person_list_cbv')

class PeriodoDetailView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseBadRequest("Requisição triste")

class PeriodoListView(View):
    def get(self, request, *args, **kwargs):
        periodos = Periodo.objects.all().order_by('p_inicio')
        form = SearchPeriodo()
        context = {'periodos': periodos, 'form': form}

        pass
        return render(request, 'periodo/periodo_list.html', context)

    def post(self, request, *args, **kwargs):
        #return HttpResponseBadRequest("Request triste")
        form = SearchPeriodo(request.POST)

        if form.is_valid():

            i_periodo = form.data.get('dt_inicio')
            f_periodo = form.data.get('dt_fim')
            #query

            periodos = Periodo.filtrar_periodo_data_inicio(i_periodo, f_periodo)

            context = {'periodos': periodos, 'form': form}
            return render(request, 'periodo/periodo_list.html', context)

        periodos = Periodo.objects.all().order_by('p_inicio')

        context = {'periodos': periodos, 'form': form}
        return render(request, 'periodo/periodo_list.html', context)