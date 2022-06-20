from django.contrib import admin
from .models import Tarefa


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'feito', 'slug', 'dataHora', 'atualizacao')
    list_editable = ('feito',)
    search_fields = ('titulo',)


