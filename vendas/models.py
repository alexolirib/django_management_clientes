from django.db import models
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from django.db.models import Sum,F,FloatField
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
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    imposto = models.DecimalField(max_digits=5, decimal_places=2, default=0)
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

    def calcular_total(self):
        tot = self.itensdopedido_set.all().aggregate(
            tot_ped = Sum((F('quantidade') * F('produto__preco')) - F('desconto'), output_field=FloatField())
        )['tot_ped'] #coloco o campo que vai retornar para o tot

        tot = tot - float(self.imposto) or 0 - float(self.desconto) or 0
        self.valor = tot
        # self.save()
        #se atualizar o desconto no cabeçalho
        Venda.objects.filter(id=self.id).update(valor=tot)

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
    quantidade = models.FloatField(default=1)
    # desconto específico para cada produto
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.venda.numero} - {self.venda.person} - {self.produto.descricao}"

# select sum(produtos_produto.preco * vendas_itensdopedido.quantidade)
# from vendas_venda, vendas_itensdopedido, produtos_produto
# where vendas_venda.id = vendas_itensdopedido.venda_id
# and  produtos_produto.id = vendas_itensdopedido.produto_id
# and vendas_venda.numero = '855';

# from django.db.models import Sum,F,FloatField
# v = Venda.objects.all()
# v.itensdopedido_set.all().aggregate(tot_ped=Sum(F('quantidade') * F('produto__preco'), output_field=FloatField()))
# {'tot_ped': 23.0}


@receiver(post_save, sender=ItensDoPedido)
def update_ItensDePedido_total(sender, instance, **kwargs):
    instance.venda.calcular_total()


@receiver(post_save, sender=Venda)
def update_vendas_total(sender, instance, **kwargs):
    instance.calcular_total()
