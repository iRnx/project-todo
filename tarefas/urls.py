from django.urls import path
from . import views

urlpatterns = [
    path('', views.listas_de_tarefas, name='listas_de_tarefas'),
    path('tarefas/<slug:slug>', views.tarefa, name='tarefa'),
]
