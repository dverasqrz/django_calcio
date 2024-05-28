# campeonatos/urls.py

from django.urls import path
from .views import CampeonatoListView, CampeonatoDetailView

urlpatterns = [
    path('', CampeonatoListView.as_view(), name='campeonato_list'),
    path('<int:pk>/', CampeonatoDetailView.as_view(), name='campeonato_detail'),
]
