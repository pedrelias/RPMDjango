# Generated by Django 5.0.8 on 2024-08-13 23:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaAutomobilismo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('fundacao', models.DateField()),
                ('site_oficial', models.URLField()),
            ],
            options={
                'verbose_name': 'Categoria do Automobilismo',
                'verbose_name_plural': 'Categorias do Automobilismo',
            },
        ),
        migrations.CreateModel(
            name='Cidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Cidade',
                'verbose_name_plural': 'Cidades',
            },
        ),
        migrations.CreateModel(
            name='Corrida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data', models.DateField()),
                ('circuito', models.CharField(max_length=100)),
                ('numero_voltas', models.IntegerField()),
                ('categoria', models.CharField(max_length=100)),
                ('vencedor', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Corrida',
                'verbose_name_plural': 'Corridas',
            },
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
                ('fundacao', models.IntegerField()),
                ('site_oficial', models.URLField()),
            ],
            options={
                'verbose_name': 'Equipe',
                'verbose_name_plural': 'Equipes',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('continente', models.CharField(max_length=100)),
                ('codigo_iso', models.CharField(max_length=2)),
            ],
            options={
                'verbose_name': 'Pais',
                'verbose_name_plural': 'Paises',
            },
        ),
        migrations.CreateModel(
            name='Piloto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('pais', models.CharField(max_length=100)),
                ('equipe', models.CharField(max_length=100)),
                ('podios', models.IntegerField()),
                ('pole_positions', models.IntegerField()),
                ('vitorias', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Piloto',
                'verbose_name_plural': 'Pilotos',
            },
        ),
        migrations.CreateModel(
            name='Circuito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cidades')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pais')),
            ],
            options={
                'verbose_name': 'Circuito',
                'verbose_name_plural': 'Circuitos',
            },
        ),
        migrations.CreateModel(
            name='Calendario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('categoria', models.CharField(max_length=100)),
                ('circuito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.circuito')),
                ('corrida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.corrida')),
            ],
            options={
                'verbose_name': 'Calendario',
            },
        ),
        migrations.CreateModel(
            name='Montadora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('fundacao', models.IntegerField()),
                ('site_oficial', models.URLField()),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cidades')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pais')),
            ],
            options={
                'verbose_name': 'Montadora',
                'verbose_name_plural': 'Montadoras',
            },
        ),
        migrations.AddField(
            model_name='cidades',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pais'),
        ),
        migrations.CreateModel(
            name='CanalTransmissao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('site_oficial', models.URLField()),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pais')),
            ],
            options={
                'verbose_name': 'Canal de Transmissao',
                'verbose_name_plural': 'Canais de Transmissao',
            },
        ),
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
                ('motor', models.CharField(max_length=100)),
                ('peso', models.IntegerField()),
                ('potencia', models.IntegerField()),
                ('equipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.equipe')),
                ('montadora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.montadora')),
                ('piloto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carros', to='app.piloto')),
            ],
            options={
                'verbose_name': 'Carro',
                'verbose_name_plural': 'Carros',
            },
        ),
        migrations.CreateModel(
            name='Pontuacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicao', models.IntegerField()),
                ('pontos', models.IntegerField()),
                ('corrida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.corrida')),
                ('piloto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.piloto')),
            ],
            options={
                'verbose_name': 'Pontuacao',
            },
        ),
        migrations.CreateModel(
            name='Transmissao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario_inicio', models.DateTimeField()),
                ('canal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.canaltransmissao')),
                ('corrida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.corrida')),
            ],
            options={
                'verbose_name': 'Transmissao',
                'verbose_name_plural': 'Transmissoes',
            },
        ),
    ]
