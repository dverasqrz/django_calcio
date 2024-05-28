# campeonatos/admin.py

from django.contrib import admin
from .models import Campeonato, Time, Jogo

admin.site.register(Campeonato)
admin.site.register(Time)
admin.site.register(Jogo)
