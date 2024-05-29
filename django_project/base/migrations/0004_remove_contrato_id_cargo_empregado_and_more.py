# Generated by Django 5.0.1 on 2024-03-11 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contrato',
            name='id_cargo_empregado',
        ),
        migrations.RemoveField(
            model_name='contrato',
            name='id_convenio',
        ),
        migrations.RemoveField(
            model_name='contrato',
            name='id_empregado',
        ),
        migrations.RemoveField(
            model_name='meta',
            name='codigo_convenio',
        ),
        migrations.DeleteModel(
            name='Atividade',
        ),
        migrations.DeleteModel(
            name='Cargo',
        ),
        migrations.DeleteModel(
            name='Contrato',
        ),
        migrations.DeleteModel(
            name='Empregado',
        ),
        migrations.DeleteModel(
            name='Convenio',
        ),
        migrations.DeleteModel(
            name='Meta',
        ),
    ]