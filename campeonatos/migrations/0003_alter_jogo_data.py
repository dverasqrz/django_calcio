# Generated by Django 5.0.6 on 2024-05-30 02:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campeonatos', '0002_campeonato_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogo',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
