# Generated by Django 4.0.4 on 2022-06-04 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0009_remove_collect_user_id_alter_collect_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collect',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
