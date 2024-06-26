# Generated by Django 5.0.6 on 2024-05-28 23:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('tipo', models.CharField(choices=[('estaduais', 'Estaduais'), ('nacionais', 'Nacionais')], default='estaduais', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('campeonato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='times', to='campeonatos.campeonato')),
            ],
        ),
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('gols_time_casa', models.IntegerField(blank=True, null=True)),
                ('gols_time_fora', models.IntegerField(blank=True, null=True)),
                ('campeonato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jogos', to='campeonatos.campeonato')),
                ('time_casa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jogos_casa', to='campeonatos.time')),
                ('time_fora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jogos_fora', to='campeonatos.time')),
            ],
        ),
    ]
