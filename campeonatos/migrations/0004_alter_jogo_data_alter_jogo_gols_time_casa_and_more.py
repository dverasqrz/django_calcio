# Generated by Django 5.0.6 on 2024-05-30 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campeonatos', '0003_alter_jogo_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogo',
            name='data',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='jogo',
            name='gols_time_casa',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='jogo',
            name='gols_time_fora',
            field=models.IntegerField(default=-1),
        ),
    ]
