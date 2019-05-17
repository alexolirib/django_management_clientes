from django.db import models
from django.db.models import Q


class Document(models.Model):
    num_doc = models.CharField(max_length=50)

    def __str__(self):
        return self.num_doc


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)
    doc = models.OneToOneField(Document, null=True, blank=True, on_delete=models.CASCADE)

    #funçao string sempre mostre o nome da pessa
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Produto(models.Model):
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.descricao

from functools import reduce
class Venda(models.Model):
    numero = models.CharField(max_length=7)
    desconto = models.DecimalField(max_digits=5, decimal_places=2)
    imposto = models.DecimalField(max_digits=5, decimal_places=2)
    person = models.ForeignKey(Person, null=True, blank=True, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto, blank=True)

    def get_total(self):
        return (self.value_all_sale() - self.calculate_tax_discount())

    def value_all_sale(self):
        prices = [x.preco for x in self.produtos.all()]
        sum_prices = reduce(lambda x, y: x+y, prices)
        return float(sum_prices)

    #sobrescrevendo método save
    # def save(self, filename="Venda", *args, **kwargs):
    #     super(Venda, self).save(*args, **kwargs)

    @staticmethod
    def update_price_discount(discount, tax):
        for venda in Venda.objects.all():
            venda.imposto = tax
            venda.desconto = discount
            venda.save()

    def calculate_tax_discount(self):
        all = self.value_all_sale() * (float(self.imposto)/100)
        all += self.value_all_sale() * (float(self.desconto)/100)
        return all

    def __str__(self):
        return self.numero

class Periodo(models.Model):
    nome = models.CharField(max_length=60,null=True)
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

