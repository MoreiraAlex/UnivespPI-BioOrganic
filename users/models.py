from email.policy import default
from statistics import mode
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    cep = models.CharField(name='CEP', max_length=9, default= '')
    uf = models.CharField(name='Estado', max_length=20, default= '')
    cidade = models.CharField(name='Cidade', max_length=30, default= '')
    block = models.CharField(name='Bairro', max_length=30, default= '')
    address = models.CharField(name='Endereço', max_length=50, default= '')
    number = models.CharField(name='Numero', max_length=10, default= '')
    complement = models.CharField(name='Complemento', max_length=30, default= '', blank=True)
    phone = models.CharField(name='Telefone', max_length=14, default= '')
    insta = models.CharField(name='Instagram', max_length=30, default= '', blank=True)
    descard = models.BooleanField( name='Realiza descarte de óleo frequentemente?', default=False, choices=[
        (True, 'Sim'),
        (False, 'Não')
    ])
    time = models.CharField(max_length=30, name='Se sim, a cada quanto tempo?', default= '', choices=[
        ('Não descarta', 'Não descarto'),
        ('Duas semanas', 'A cada duas semanas'),
        ('Um mês', 'A cada um mês'),
        ('Dois meses', 'A cada dois meses')
    ])
    full = models.BooleanField(name='Completo', default=False)

