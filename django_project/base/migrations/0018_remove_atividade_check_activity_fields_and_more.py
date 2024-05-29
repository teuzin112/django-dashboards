# Generated by Django 5.0.1 on 2024-04-04 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_alter_empregado_genero'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='atividade',
            name='check_activity_fields',
        ),
        migrations.AddConstraint(
            model_name='atividade',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('meta__isnull', False), ('fp_nit__isnull', True)), models.Q(('meta__isnull', True), ('fp_nit__isnull', False)), _connector='OR'), name='check_atividade_fields'),
        ),
    ]