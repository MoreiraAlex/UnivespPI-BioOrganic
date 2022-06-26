from email.policy import default
from statistics import mode
from tabnanny import verbose
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name = models.CharField(verbose_name='Nome ou razão social', max_length=150, default='')
    last_name = models.CharField(verbose_name='Sobrenome ou nome fantasia', max_length=150, default='')
    cpf_cnpj = models.CharField(verbose_name='CPF ou CNPJ', max_length=15, default='')
    cep = models.CharField(verbose_name='CEP', max_length=9, default= '')
    uf = models.CharField(verbose_name='Estado', max_length=20, default= '')
    city = models.CharField(verbose_name='Cidade', max_length=30, default= '')
    block = models.CharField(verbose_name='Bairro', max_length=30, default= '')
    address = models.CharField(verbose_name='Endereço', max_length=50, default= '')
    number = models.CharField(verbose_name='Numero', max_length=10, default= '')
    complement = models.CharField(verbose_name='Complemento', max_length=30, default= '', blank=True)
    liters = models.IntegerField(verbose_name='Média de óleo utilzado por mês(Lts)', default=0)
    phone = models.CharField(verbose_name='Telefone', max_length=14, default= '')
    insta = models.CharField(verbose_name='Instagram', max_length=30, default= '', blank=True)
    full = models.BooleanField(verbose_name='Completo', default=False)

