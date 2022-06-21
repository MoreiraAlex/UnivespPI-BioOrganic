from datetime import datetime
from django.db import models
from users.models import User

class Collect(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=30, default= '')
    liters = models.IntegerField(verbose_name='Quantidade aproximada de óleo (Lts)', default=0)
    cep = models.CharField(verbose_name='CEP', max_length=9, default= '')
    uf = models.CharField(verbose_name='Estado', max_length=20, default= '')
    city = models.CharField(verbose_name='Cidade', max_length=30, default= '')
    block = models.CharField(verbose_name='Bairro', max_length=30, default= '')
    address = models.CharField(verbose_name='Endereço', max_length=50, default= '')
    number = models.CharField(verbose_name='Numero', max_length=10, default= '')
    complement = models.CharField(verbose_name='Complemento', max_length=30, default= '', blank=True)
    date = models.DateField(verbose_name='Data da coleta', default=datetime.now)
    time = models.CharField(max_length=20, verbose_name='Horario da coleta', default='', choices=[
        ('8:00hrs - 12:00hrs','8:00hrs - 12:00hrs'),
        ('13:00hrs - 18:00hrs', '13:00hrs - 18:00hrs'),
    ])
    img = models.ImageField(verbose_name='Foto do recipiente com o óleo', default='', upload_to='', blank=True)
    created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, default='Pendente', choices=[
        ('Pendente','Pendente'),
        ('Aprovada', 'Aprovada'),
        ('Reprovada', 'Reprovada'),
        ('Concluida', 'Concluida'),
        ('Cancelada', 'Cancelada'),
    ])  
    obs = models.TextField(max_length=50, default='')
    real_liters = models.FloatField(verbose_name='Quantidade real de óleo (Lts)', default=0)

    def __str__(self):
        return ('#' + str(self.id))

