# Generated by Django 5.0.1 on 2024-02-13 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0003_remove_avaliacao_estrelas_estrela_avaliacao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estrela',
            old_name='user',
            new_name='usuario',
        ),
        migrations.RemoveField(
            model_name='estrela',
            name='avaliacao',
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='estrelas',
            field=models.ManyToManyField(related_name='avaliacoes', to='avaliacoes.estrela'),
        ),
    ]
