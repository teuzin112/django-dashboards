# Generated by Django 5.0.1 on 2024-06-26 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_remove_meta_indicador_atividade_indicador'),
    ]

    operations = [
        migrations.AddField(
            model_name='empregado',
            name='username',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
