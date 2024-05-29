# Generated by Django 5.0.1 on 2024-03-13 14:06

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Andamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcent_executada', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('data', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='atividade',
            name='link_exec',
            field=models.CharField(max_length=4000, null=True),
        ),
        migrations.AddField(
            model_name='atividade',
            name='link_img',
            field=models.CharField(max_length=4000, null=True),
        ),
        migrations.AddField(
            model_name='atividade',
            name='peso',
            field=models.IntegerField(choices=[(1, '1'), (3, '3'), (6, '6')], null=True),
        ),
        migrations.AddField(
            model_name='empregado',
            name='matricula_cracha',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evento',
            name='categoria_participantes',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evento',
            name='denominacao',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evento',
            name='participantes',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Cargo_Empregado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField()),
                ('data_final', models.DateField(null=True)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.cargo')),
                ('empregado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.empregado')),
            ],
        ),
        migrations.AlterField(
            model_name='contrato',
            name='cargo_empregado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.cargo_empregado'),
        ),
    ]
