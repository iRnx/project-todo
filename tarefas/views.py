from django.shortcuts import render, get_object_or_404
from .models import Tarefa


def listas_de_tarefas(request):
    listas = Tarefa.objects.all()
    return render(request, 'tarefas/listas_de_tarefas.html', {'listas': listas})


def tarefa(request, slug):
    tarefa = get_object_or_404(Tarefa, slug=slug)
    return render(request, 'tarefas/tarefa.html', {'tarefa': tarefa})


