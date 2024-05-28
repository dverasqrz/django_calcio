# campeonatos/forms.py
from django import forms
from .models import Campeonato

class CampeonatoForm(forms.ModelForm):
    class Meta:
        model = Campeonato
        fields = ['nome', 'data_inicio', 'data_fim', 'tipo']
