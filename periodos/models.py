from django.db import models
from django.db.models import Q


class Periodo(models.Model):
    nome = models.CharField(max_length=60, null=True)
    p_inicio = models.DateField()
    p_fim = models.DateField()

    def __str__(self):
        return str(self.p_inicio) + " - " + str(self.p_fim)

    # lte <= Menor que ou igual.
    # gte >= Maior que ou igual.
    # range = BETWEEN
    def filtrar_periodo_data_inicio(dt_inicio, dt_fim):
        return Periodo.objects.filter(
            (Q(p_inicio__gte=dt_inicio) & Q(p_fim__lte=dt_inicio))
            |
            (Q(p_inicio__lte=dt_inicio) & Q(p_fim__gte=dt_inicio))
            |
            (Q(p_inicio__gte=dt_fim) & Q(p_fim__lte=dt_fim))
            |
            (Q(p_inicio__lte=dt_fim) & Q(p_fim__gte=dt_fim))
            |
            (Q(p_inicio__range=(dt_inicio, dt_fim)))
            |
            (Q(p_fim__range=(dt_inicio, dt_fim)))
        ).order_by('p_inicio')
