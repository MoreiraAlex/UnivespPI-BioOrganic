# Generated by Django 4.0.4 on 2022-06-06 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0012_alter_collect_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collect',
            name='img',
            field=models.ImageField(blank=True, default='', upload_to='media', verbose_name='Foto do recipiente com o óleo'),
        ),
    ]
