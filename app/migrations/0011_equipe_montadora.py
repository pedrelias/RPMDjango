# Generated by Django 5.0.8 on 2024-08-26 22:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_equipe_categoria_automobilismo'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipe',
            name='montadora',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.montadora'),
        ),
    ]
