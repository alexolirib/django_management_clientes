from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from functools import reduce
from client.models import Person
from produtos.models import Produto

def atualiza_vendas():
    vendas = Venda.objects.all()
    for v in vendas:
        v.valor = v.get_total()
        v.save()


class Venda(models.Model):
    numero = models.CharField(max_length=7)
    valor = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    desconto = models.DecimalField(max_digits=5, decimal_places=2)
    imposto = models.DecimalField(max_digits=5, decimal_places=2)
    person = models.ForeignKey(Person, null=True, blank=True, on_delete=models.CASCADE)
    nfe_emitida = models.BooleanField(default=False)

    # def get_total(self):
    #     return self.value_all_sale() - self.calculate_tax_discount()
    #
    # def value_all_sale(self):
    #     if len(self.produtos.all()) != 0:
    #         prices = [x.preco for x in self.produtos.all()]
    #         sum_prices = reduce(lambda x, y: x+y, prices)
    #         return float(sum_prices)
    #     else:
    #         return 0

    # sobrescrevendo método save
    # def save(self, filename="Venda", *args, **kwargs):
    #     super(Venda, self).save(*args, **kwargs)

    @staticmethod
    def update_price_discount(discount, tax):
        for venda in Venda.objects.all():
            venda.imposto = tax
            venda.desconto = discount
            venda.save()

    def calculate_tax_discount(self):
        all = self.value_all_sale() * (float(self.imposto) / 100)
        all += self.value_all_sale() * (float(self.desconto) / 100)
        return all

    def __str__(self):
        return self.numero

# through os elementos da relação (como se fosse uma trigger
# @receiver(m2m_changed, sender=Venda.produtos.through)
def update_vendas_total(sender, instance, **kwargs):
    instance.save()
    instance.valor = instance.get_total()
    instance.save()
    # Venda.objects.filter(id=instance.id).update(valor=total)





class ItensDoPedido(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.FloatField()
    # desconto específico para cada produto
    desconto = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.venda.numero} - {self.venda.person} - {self.produto.descricao}"

