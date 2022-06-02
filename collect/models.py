from datetime import datetime
from django.db import models
from users.models import User

class Collect(models.Model):
    #first_name = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    liters = models.IntegerField(verbose_name='Quantidade aproximada de óleo (Lts)', default=0)
    cep = models.CharField(verbose_name='CEP', max_length=9, default= '')
    uf = models.CharField(verbose_name='Estado', max_length=20, default= '')
    city = models.CharField(verbose_name='Cidade', max_length=30, default= '')
    block = models.CharField(verbose_name='Bairro', max_length=30, default= '')
    address = models.CharField(verbose_name='Endereço', max_length=50, default= '')
    number = models.CharField(verbose_name='Numero', max_length=10, default= '')
    complement = models.CharField(verbose_name='Complemento', max_length=30, default= '', blank=True)
    img = models.ImageField(verbose_name='Foto do recipiente com o óleo', default='', blank=True)
    date = models.DateField(verbose_name='Data da coleta', default=datetime.now)
    code = models.IntegerField(default=0, auto_created=True)

