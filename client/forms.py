from django.forms import ModelForm
from .models import Person
from django import forms

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']


class SearchPeriodo(forms.Form):
    dt_inicio = forms.DateField()
    dt_fim = forms.DateField()
