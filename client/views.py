from django.shortcuts import render, redirect, get_object_or_404

from client.forms import PersonForm
from client.models import Person


def persons_list(request):
    #lista todos os clientes
    persons = Person.objects.all()
    return render(request, 'person.html', {'v_persons': persons})

def persons_new(request):
    #verifica se já tem algo, se não envia vazio
    #request.FILES - arquivos de midias que estão sendo enviados
    form = PersonForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(persons_list)
    return render(request, 'person_form.html', {'form': form})

def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect(persons_list)
    return render(request, 'person_form.html', {'form': form})

def persons_delete(request, id):
    person = get_object_or_404(Person,  pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if request.method == 'POST':
        person.delete()
        return redirect(persons_list)
    return render(request, 'person_delete_confirm.html', {'person': person, 'form':form})
