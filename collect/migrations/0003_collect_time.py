# Generated by Django 4.0.4 on 2022-06-03 22:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0002_remove_collect_teste_collect_address_collect_block_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='collect',
            name='time',
            field=models.TimeField(default=datetime.datetime.now, verbose_name='Horario da coleta'),
        ),
    ]
