# campeonatos/views.py

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Campeonato
from .forms import CampeonatoForm
from collections import defaultdict

class OnlySuperUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.times.count() % 2 == 0:
            context['jogos_por_rodada'] = self.get_jogos_por_rodada()
        else:
            context['jogos'] = self.object.get_jogos_validos().order_by('data')
        return context

    def get_jogos_por_rodada(self):
        jogos_por_rodada = defaultdict(list)
        for jogo in self.object.jogos.all().order_by('rodada', 'data'):
            jogos_por_rodada[jogo.rodada].append(jogo)
        return dict(jogos_por_rodada)

class CampeonatoCreateView(OnlySuperUserMixin, CreateView):
    model = Campeonato
    form_class = CampeonatoForm
    template_name = 'campeonatos/campeonato_form.html'
    success_url = reverse_lazy('campeonato_list')

class CampeonatoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Campeonato
    form_class = CampeonatoForm
    template_name = 'campeonatos/campeonato_form.html'
    success_url = reverse_lazy('campeonato_list')

    def test_func(self):
        campeonato = self.get_object()
        return self.request.user.is_superuser or self.request.user in campeonato.users.all()

class CampeonatoDeleteView(OnlySuperUserMixin, DeleteView):
    model = Campeonato
    success_url = reverse_lazy('campeonato_list')

@login_required
def user_campeonatos(request):
    campeonatos = request.user.campeonatos.all()
    return render(request, 'campeonatos/user_campeonatos.html', {'campeonatos': campeonatos})

def index(request):
    return render(request, 'campeonatos/index.html')
