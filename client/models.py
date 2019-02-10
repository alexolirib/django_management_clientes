from django.db import models
#para criar - python manage.py startapp client
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)

    #funçao string sempre mostre o nome da pessa
    def __str__(self):
        return self.first_name + ' ' + self.last_name
