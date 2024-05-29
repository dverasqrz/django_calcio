# campeonatos/urls.py

from django.urls import path
from .views import CampeonatoListView, CampeonatoDetailView, CampeonatoCreateView, CampeonatoUpdateView, CampeonatoDeleteView, user_campeonatos

urlpatterns = [
    path('', CampeonatoListView.as_view(), name='campeonato_list'),
    path('<int:pk>/', CampeonatoDetailView.as_view(), name='campeonato_detail'),
    path('add/', CampeonatoCreateView.as_view(), name='campeonato_add'),
    path('<int:pk>/edit/', CampeonatoUpdateView.as_view(), name='campeonato_update'),
    path('<int:pk>/delete/', CampeonatoDeleteView.as_view(), name='campeonato_delete'),
    path('meus_campeonatos/', user_campeonatos, name='user_campeonatos'),
]
