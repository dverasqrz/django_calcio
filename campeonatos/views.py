# campeonatos/views.py

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Campeonato
from .forms import CampeonatoForm

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
