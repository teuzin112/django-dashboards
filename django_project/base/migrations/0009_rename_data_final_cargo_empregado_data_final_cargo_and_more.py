# Generated by Django 5.0.1 on 2024-03-14 14:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cargo_empregado',
            old_name='data_final',
            new_name='data_final_cargo',
        ),
        migrations.RenameField(
            model_name='cargo_empregado',
            old_name='data_inicio',
            new_name='data_inicio_cargo',
        ),
        migrations.AlterField(
            model_name='atividade',
            name='meta',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.meta'),
        ),
        migrations.CreateModel(
            name='Fp_nit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=2000)),
                ('descricao', models.TextField(null=True)),
                ('data_inicio', models.DateField()),
                ('data_final', models.DateField()),
                ('meta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.meta')),
            ],
        ),
        migrations.AddField(
            model_name='atividade',
            name='fp_nit',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.fp_nit'),
        ),
        migrations.AddConstraint(
            model_name='atividade',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('meta__isnull', False), ('fp_nit__isnull', True)), models.Q(('meta__isnull', True), ('fp_nit__isnull', False)), _connector='OR'), name='check_activity_fields'),
        ),
    ]