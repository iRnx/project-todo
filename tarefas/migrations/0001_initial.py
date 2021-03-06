# Generated by Django 4.0.5 on 2022-06-20 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=125)),
                ('descricao', models.TextField()),
                ('feito', models.CharField(choices=[('feito', 'Feito'), ('fazendo', 'Fazendo')], max_length=7)),
                ('slug', models.SlugField(blank=True, editable=False)),
                ('dataHora', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
