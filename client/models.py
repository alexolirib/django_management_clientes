from django.db import models
#para criar - python manage.py startapp client
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

class Venda(models.Model):
    numero = models.CharField(max_length=7)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    desconto = models.DecimalField(max_digits=5, decimal_places=2)
    imposto = models.DecimalField(max_digits=5, decimal_places=2)
    person = models.ForeignKey(Person, null=True, blank=True, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto, blank=True)

    def __str__(self):
        return self.numero

