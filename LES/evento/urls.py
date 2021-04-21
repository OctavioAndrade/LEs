from django.urls import path
from .views import (home, vieweventos, criarinscricao)

urlpatterns = [
	path('', home, name='home'),
	path('eventos/', vieweventos, name='vieweventos'),
	path('eventos/inscricao', criarinscricao, name='criarinscricao')
]