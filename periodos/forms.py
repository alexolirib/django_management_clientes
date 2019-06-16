from django import forms


class SearchPeriodo(forms.Form):
    dt_inicio = forms.DateField()
    dt_fim = forms.DateField()
