# Generated by Django 4.0.4 on 2022-06-09 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0017_alter_collect_obs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collect',
            name='obs',
            field=models.TextField(default='', max_length=50),
        ),
    ]
