from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarefa
from .form import TarefaForm


def listas_de_tarefas(request):
    listas = Tarefa.objects.all()
    return render(request, 'tarefas/listas_de_tarefas.html', {'listas': listas})


def tarefa(request, slug):
    tarefa = get_object_or_404(Tarefa, slug=slug)
    return render(request, 'tarefas/tarefa.html', {'tarefa': tarefa})


def adicionar_tarefa(request):

    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            formulario = form.save(commit=False)
            formulario.feito = 'fazendo'
            formulario.save()
            return redirect('/')

    if request.method == 'GET':
        form = TarefaForm()
        return render(request, 'tarefas/adicionar_tarefa.html', {'form': form})


def editar_tarefa(request, slug):
    tarefa = get_object_or_404(Tarefa, slug=slug)

    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('/')

    if request.method == 'GET':
        form = TarefaForm(instance=tarefa)
        return render(request, 'tarefas/editar_tarefa.html', {'tarefa': tarefa, 'form': form})
