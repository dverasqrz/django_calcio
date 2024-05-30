# futebol/urls.py

from django.contrib import admin
from django.urls import path, include
from campeonatos.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('campeonatos/', include('campeonatos.urls')),
    path('', index, name='index'),  # Adiciona a rota para a página inicial
]
