from django.db.models import signals
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Tarefa(models.Model):

    titulo = models.CharField(max_length=125)
    descricao = models.TextField()

    STATUS = (
        ('feito', 'Feito'),
        ('fazendo', 'Fazendo'),
    )

    feito = models.CharField(choices=STATUS, max_length=7)
    slug = models.SlugField(blank=True, editable=False)
    dataHora = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Tarefas'

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('tarefa', kwargs={'slug': self.slug})

    # uma forma de fazer o slug sem usar signals #
    """def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.titulo)
        return super().save(*args, **kwargs)"""


def tarefa_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.titulo)


signals.pre_save.connect(tarefa_pre_save, sender=Tarefa)


