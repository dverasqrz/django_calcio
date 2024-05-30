# campeonatos/utils.py

from datetime import timedelta, datetime
from django.utils import timezone
from .models import Campeonato, Time, Jogo
from collections import defaultdict

def generate_games_for_championship(championship_id):
    try:
        campeonato = Campeonato.objects.get(pk=championship_id)
    except Campeonato.DoesNotExist:
        return f"Campeonato com ID {championship_id} não existe."

    times = list(campeonato.times.all())
    num_times = len(times)
    if num_times < 2:
        return "Não há times suficientes para criar partidas."

    jogos = []
    start_date = campeonato.data_inicio
    game_date = datetime.combine(start_date, datetime.strptime("13:00", "%H:%M").time())
    game_date = timezone.make_aware(game_date)

    if num_times % 2 == 0:
        # Número de times par, usar a abordagem de rodadas
        rodada = 1
        for i in range(num_times - 1):
            for j in range(num_times // 2):
                home_team = times[j]
                away_team = times[num_times - 1 - j]

                jogos.append(Jogo(campeonato=campeonato, time_casa=home_team, time_fora=away_team, data=game_date, rodada=rodada))
                jogos.append(Jogo(campeonato=campeonato, time_casa=away_team, time_fora=home_team, data=game_date + timedelta(days=num_times), rodada=rodada + num_times // 2))
                game_date += timedelta(days=1)
            rodada += 1
            times.insert(1, times.pop())
    else:
        # Número de times ímpar, jogos normais
        rodada = 1
        for i in range(num_times):
            for j in range(i + 1, num_times):
                home_team = times[i]
                away_team = times[j]

                jogos.append(Jogo(campeonato=campeonato, time_casa=home_team, time_fora=away_team, data=game_date, rodada=rodada))
                jogos.append(Jogo(campeonato=campeonato, time_casa=away_team, time_fora=home_team, data=game_date + timedelta(days=num_times), rodada=rodada))
                game_date += timedelta(days=1)
            rodada += 1

    for jogo in jogos:
        jogo.save()

    return f"{len(jogos)} jogos foram gerados para o campeonato {campeonato.nome}."
