# Generated by Django 4.0.4 on 2022-06-26 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0021_alter_collect_date_alter_collect_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collect',
            old_name='date',
            new_name='day',
        ),
    ]