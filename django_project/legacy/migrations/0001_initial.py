# Generated by Django 5.0.1 on 2024-06-21 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AtvMetas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('convenio', models.CharField(max_length=255)),
                ('meta', models.CharField(max_length=2000)),
                ('atividade', models.CharField(max_length=2000)),
                ('begin_date', models.CharField(max_length=50)),
                ('end_date', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'dashboards.atv_metas',
                'managed': False,
            },
        ),
    ]
