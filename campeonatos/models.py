# campeonatos/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Campeonato(models.Model):
    TIPO_CHOICES = [
        ('estaduais', 'Estaduais'),
        ('nacionais', 'Nacionais'),
    ]
    
    nome = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='estaduais')
    users = models.ManyToManyField(User, related_name='campeonatos')

    def __str__(self):
        return self.nome

    def get_jogos_validos(self):
        return self.jogos.filter(gols_time_casa__isnull=False, gols_time_fora__isnull=False, data__range=(self.data_inicio, self.data_fim))

    def get_classificacao(self):
        times = self.times.all()
        classificacao = {time: {'pontos': 0, 'gols_pro': 0, 'gols_contra': 0, 'saldo': 0, 'jogos': 0} for time in times}
        
        for jogo in self.get_jogos_validos():
            time_casa = jogo.time_casa
            time_fora = jogo.time_fora
            gols_casa = jogo.gols_time_casa
            gols_fora = jogo.gols_time_fora

            classificacao[time_casa]['gols_pro'] += gols_casa
            classificacao[time_casa]['gols_contra'] += gols_fora
            classificacao[time_fora]['gols_pro'] += gols_fora
            classificacao[time_fora]['gols_contra'] += gols_casa

            classificacao[time_casa]['jogos'] += 1
            classificacao[time_fora]['jogos'] += 1

            if gols_casa > gols_fora:
                classificacao[time_casa]['pontos'] += 3
            elif gols_fora > gols_casa:
                classificacao[time_fora]['pontos'] += 3
            else:
                classificacao[time_casa]['pontos'] += 1
                classificacao[time_fora]['pontos'] += 1
        
        for time in classificacao:
            classificacao[time]['saldo'] = classificacao[time]['gols_pro'] - classificacao[time]['gols_contra']

        classificacao = sorted(classificacao.items(), key=lambda x: (x[1]['pontos'], x[1]['gols_pro'], x[1]['saldo']), reverse=True)
        return classificacao

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
