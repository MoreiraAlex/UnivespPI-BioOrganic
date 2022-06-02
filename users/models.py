from email.policy import default
from statistics import mode
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    cep = models.CharField(verbose_name='CEP', max_length=9, default= '')
    uf = models.CharField(verbose_name='Estado', max_length=20, default= '')
    city = models.CharField(verbose_name='Cidade', max_length=30, default= '')
    block = models.CharField(verbose_name='Bairro', max_length=30, default= '')
    address = models.CharField(verbose_name='Endereço', max_length=50, default= '')
    number = models.CharField(verbose_name='Numero', max_length=10, default= '')
    complement = models.CharField(verbose_name='Complemento', max_length=30, default= '', blank=True)
    phone = models.CharField(verbose_name='Telefone', max_length=14, default= '')
    insta = models.CharField(verbose_name='Instagram', max_length=30, default= '', blank=True)
    descard = models.BooleanField( verbose_name='Realiza descarte de óleo frequentemente?', default=False, choices=[
        (True, 'Sim'),
        (False, 'Não')
    ])
    time = models.CharField(max_length=30, verbose_name='Se sim, a cada quanto tempo?', default= '', choices=[
        ('Não descarta', 'Não descarto'),
        ('Duas semanas', 'A cada duas semanas'),
        ('Um mês', 'A cada um mês'),
        ('Dois meses', 'A cada dois meses')
    ])
    full = models.BooleanField(verbose_name='Completo', default=False)

