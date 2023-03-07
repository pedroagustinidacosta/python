from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

# criando os edificios
class Building(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    andares = models.IntegerField()

    def __str__(self):
        return self.nome
#Criando lista dos locadores
class Renter(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    data_nascimento = models.DateField(null=True, blank=True)
    altura = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.nome
# criando os apartamentos
class Apartment(models.Model):

    edificio = models.ForeignKey(Building, on_delete=models.CASCADE)
    numero = models.CharField(max_length=10)
    quartos = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.numero} - {self.edificio.nome}"


class Rental(models.Model):
    locador = models.ForeignKey(Renter, on_delete=models.CASCADE)
    apartamento = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.locador.nome} - {self.apartamento.numero}"


