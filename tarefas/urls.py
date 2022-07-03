from django.urls import path
from . import views

urlpatterns = [
    path('', views.listas_de_tarefas, name='listas_de_tarefas'),
    path('<slug:slug>', views.tarefa, name='tarefa'),
    path('adicionar_tarefa/', views.adicionar_tarefa, name='adicionar_tarefa'),
    path('Editar_Tarefa/<slug:slug>', views.editar_tarefa, name='editar_tarefa'),
]
