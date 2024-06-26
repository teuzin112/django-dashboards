from django.db import models

class AtvMetas(models.Model):
    id = models.AutoField(primary_key=True)  # Define o campo ID como chave primária
    convenio = models.CharField(max_length=255)
    meta = models.CharField(max_length=2000)
    atividade = models.CharField(max_length=2000)
    begin_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)

    class Meta:
        managed = False  # O Django não deve tentar criar ou alterar esta tabela
        db_table = 'dashboards"."atv_metas' # Inclui o schema 'dashboards' no nome da tabela
