# campeonatos/views.py
from django.shortcuts import render, get_object_or_404
from .models import Campeonato, Time, Jogo
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .forms import CampeonatoForm

def index(request):
    return render(request, 'campeonatos/index.html')

class CampeonatoListView(ListView):
    model = Campeonato
    template_name = 'campeonatos/campeonato_list.html'
    def get_queryset(self):
        tipo = self.request.GET.get('tipo')
        if tipo:
            return Campeonato.objects.filter(tipo=tipo)
        return Campeonato.objects.all()

class CampeonatoDetailView(DetailView):
    model = Campeonato
    template_name = 'campeonatos/campeonato_detail.html'

class CampeonatoCreateView(CreateView):
    model = Campeonato
    form_class = CampeonatoForm
    template_name = 'campeonatos/campeonato_form.html'
    success_url = reverse_lazy('campeonato_list')
