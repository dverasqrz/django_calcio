# campeonatos/models.py
from django.db import models

class Campeonato(models.Model):
    TIPO_CHOICES = [
        ('estaduais', 'Estaduais'),
        ('nacionais', 'Nacionais'),
    ]
    nome = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='estaduais')  # Define um valor padrão)

    def __str__(self):
        return self.nome

class Time(models.Model):
    nome = models.CharField(max_length=100)
    campeonato = models.ForeignKey(Campeonato, related_name='times', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Jogo(models.Model):
    campeonato = models.ForeignKey(Campeonato, related_name='jogos', on_delete=models.CASCADE)
    time_casa = models.ForeignKey(Time, related_name='jogos_casa', on_delete=models.CASCADE)
    time_fora = models.ForeignKey(Time, related_name='jogos_fora', on_delete=models.CASCADE)
    data = models.DateTimeField()
    gols_time_casa = models.IntegerField(null=True, blank=True)
    gols_time_fora = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.time_casa} vs {self.time_fora}"
