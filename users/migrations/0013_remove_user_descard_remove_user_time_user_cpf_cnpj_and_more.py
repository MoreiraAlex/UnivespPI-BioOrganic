# Generated by Django 4.0.4 on 2022-06-26 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_user_descard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='descard',
        ),
        migrations.RemoveField(
            model_name='user',
            name='time',
        ),
        migrations.AddField(
            model_name='user',
            name='cpf_cnpj',
            field=models.CharField(default='', max_length=15, verbose_name='CPF ou CNPJ'),
        ),
        migrations.AddField(
            model_name='user',
            name='liters',
            field=models.FloatField(default=0, verbose_name='Média de óleo utilzado por mês(Lts)'),
        ),
    ]