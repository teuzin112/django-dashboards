from django.db import models

class AtvMetas(models.Model):
    id = models.AutoField(primary_key=True)  # Define o campo ID como chave primária
    convenio = models.CharField(max_length=255, null=True, blank=True)
    meta = models.CharField(max_length=2000, null=True, blank=True)
    atividade = models.CharField(max_length=2000, null=True, blank=True)
    begin_date = models.CharField(max_length=50, null=True, blank=True)
    end_date = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        managed = False  # O Django não deve tentar criar ou alterar esta tabela
        db_table = 'dashboards"."atv_metas' # Inclui o schema 'dashboards' no nome da tabela

class AndAtividades(models.Model):
    id = models.AutoField(primary_key=True)  # Define o campo ID como chave primária
    convenio = models.CharField(max_length=255, null=True, blank=True)
    meta = models.CharField(max_length=2000, null=True, blank=True)
    atividade = models.CharField(max_length=2000, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    link_img = models.CharField(max_length=4000, null=True, blank=True)
    link_exec = models.CharField(max_length=4000, null=True, blank=True)
    ult_atual_date = models.CharField(max_length=50, null=True, blank=True)
    perc_and = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        managed = False  # O Django não deve tentar criar ou alterar esta tabela
        db_table = 'dashboards"."and_atividades' # Inclui o schema 'dashboards' no nome da tabela

class AtvIndicadores(models.Model):
    id = models.AutoField(primary_key=True)  # Define o campo ID como chave primária
    convenio = models.CharField(max_length=255, null=True, blank=True)
    meta = models.CharField(max_length=2000, null=True, blank=True)
    atividade = models.CharField(max_length=2000, null=True, blank=True)
    indicador = models.CharField(max_length=20000, null=True, blank=True)
    begin_date = models.CharField(max_length=50, null=True, blank=True)
    end_date = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        managed = False  # O Django não deve tentar criar ou alterar esta tabela
        db_table = 'dashboards"."atv_indicadores' # Inclui o schema 'dashboards' no nome da tabela

class Employees(models.Model):
    id = models.AutoField(primary_key=True)  # Define o campo ID como chave primária
    convenio = models.CharField(max_length=2000, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    cargo = models.CharField(max_length=255, null=True, blank=True)
    graduacao = models.CharField(max_length=255, null=True, blank=True)
    atuacao = models.CharField(max_length=255, null=True, blank=True)
    genero = models.CharField(max_length=255, null=True, blank=True)
    nascimento = models.CharField(max_length=50, null=True, blank=True)
    data_contratacao = models.CharField(max_length=255, null=True, blank=True)
    data_venc_contrato = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        managed = False  # O Django não deve tentar criar ou alterar esta tabela
        db_table = 'dashboards"."employees' # Inclui o schema 'dashboards' no nome da tabela

class Eventos(models.Model):
    id = models.AutoField(primary_key=True)
    convenio = models.CharField(max_length=2000, null=True, blank=True)
    den_event = models.CharField(max_length=2000, null=True, blank=True)
    part_evento = models.CharField(max_length=2000, null=True, blank=True)
    date_evento = models.CharField(max_length=50, null=True, blank=True)
    desc_evento = models.CharField(max_length=8000, null=True, blank=True)
    cat_evento = models.CharField(max_length=2000, null=True, blank=True)

    class Meta:
        managed = False  # O Django não deve tentar criar ou alterar esta tabela
        db_table = 'dashboards"."eventos' # Inclui o schema 'dashboards' no nome da tabela

class ExecFinanceira(models.Model):
    id = models.AutoField(primary_key=True)
    convenio = models.CharField(max_length=2000, null=True, blank=True)
    orc_total = models.CharField(max_length=255, null=True, blank=True)  # Ajustado para varchar
    rep_recebidos = models.CharField(max_length=255, null=True, blank=True)  # Ajustado para varchar
    saldo_receber = models.CharField(max_length=255, null=True, blank=True)  # Ajustado para varchar
    rendimento = models.CharField(max_length=255, null=True, blank=True)  # Ajustado para varchar
    total_realizado = models.CharField(max_length=255, null=True, blank=True)  # Ajustado para varchar
    total_empenhado = models.CharField(max_length=255, null=True, blank=True)  # Ajustado para varchar
    saldo_executar = models.CharField(max_length=255, null=True, blank=True)  # Ajustado para varchar
    data = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        managed = False  # O Django não deve tentar criar ou alterar esta tabela
        db_table = 'dashboards"."execfinanceira' # Inclui o schema 'dashboards' no nome da tabela

class ExecValores(models.Model):
    id = models.AutoField(primary_key=True)
    convenio = models.CharField(max_length=2000, null=True, blank=True)
    desc_execute = models.CharField(max_length=2000, null=True, blank=True)
    aloc = models.CharField(max_length=50, null=True, blank=True)
    custo = models.CharField(max_length=255, null=True, blank=True)  # Ajustado para varchar
    meta = models.CharField(max_length=255, null=True, blank=True)
    rubrica = models.CharField(max_length=255, null=True, blank=True)
    data = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        managed = False  # O Django não deve tentar criar ou alterar esta tabela
        db_table = 'dashboards"."execvalores' # Inclui o schema 'dashboards' no nome da tabela


class FpsNit(models.Model):
    id = models.AutoField(primary_key=True)  # Define o campo ID como chave primária
    fpname = models.CharField(max_length=2000, null=True, blank=True)
    meta = models.CharField(max_length=2000, null=True, blank=True)
    atividade = models.CharField(max_length=2000, null=True, blank=True)
    begin_date = models.CharField(max_length=50, null=True, blank=True)
    end_date = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        managed = False  # O Django não deve tentar criar ou alterar esta tabela
        db_table = 'dash_nit"."fps_nit' # Inclui o schema 'dashboards' no nome da tabela


class AtvMetasNit(models.Model):
    id = models.AutoField(primary_key=True)  # Define o campo ID como chave primária
    meta = models.CharField(max_length=2000, null=True, blank=True)
    atividade = models.CharField(max_length=2000, null=True, blank=True)
    begin_date = models.CharField(max_length=50, null=True, blank=True)
    end_date = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        managed = False  # O Django não deve tentar criar ou alterar esta tabela
        db_table = 'dash_nit"."atv_metas_nit' # Inclui o schema 'dashboards' no nome da tabela

class AndAtividadesNit(models.Model):
    id = models.AutoField(primary_key=True)  # Define o campo ID como chave primária
    fpname = models.CharField(max_length=2000, null=True, blank=True)
    meta = models.CharField(max_length=2000, null=True, blank=True)
    atividade = models.CharField(max_length=2000, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    link_img = models.CharField(max_length=4000, null=True, blank=True)
    link_exec = models.CharField(max_length=4000, null=True, blank=True)
    ult_atual_date = models.CharField(max_length=50, null=True, blank=True)
    perc_and = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        managed = False  # O Django não deve tentar criar ou alterar esta tabela
        db_table = 'dash_nit"."and_atividades_nit' # Inclui o schema 'dashboards' no nome da tabela

class EmployeesNit(models.Model):
    id = models.AutoField(primary_key=True)  # Define o campo ID como chave primária
    username = models.CharField(max_length=255, null=True, blank=True)
    cargo = models.CharField(max_length=255, null=True, blank=True)
    graduacao = models.CharField(max_length=255, null=True, blank=True)
    atuacao_nit = models.CharField(max_length=255, null=True, blank=True)
    genero = models.CharField(max_length=255, null=True, blank=True)
    nascimento = models.CharField(max_length=50, null=True, blank=True)
    data_contratacao = models.CharField(max_length=255, null=True, blank=True)
    data_venc_contrato = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        managed = False  # O Django não deve tentar criar ou alterar esta tabela
        db_table = 'dash_nit"."employees_nit' # Inclui o schema 'dashboards' no nome da tabela

class EventosNit(models.Model):
    id = models.AutoField(primary_key=True)
    den_event = models.CharField(max_length=2000, null=True, blank=True)
    part_evento = models.CharField(max_length=2000, null=True, blank=True)
    date_evento = models.CharField(max_length=50, null=True, blank=True)
    desc_evento = models.CharField(max_length=8000, null=True, blank=True)
    cat_evento = models.CharField(max_length=2000, null=True, blank=True)

    class Meta:
        managed = False  # O Django não deve tentar criar ou alterar esta tabela
        db_table = 'dash_nit"."eventos_nit' # Inclui o schema 'dashboards' no nome da tabela

class ExecFinanceiraNit(models.Model):
    id = models.AutoField(primary_key=True)
    orc_total = models.CharField(max_length=255, null=True, blank=True)  # Ajustado para varchar
    rep_recebidos = models.CharField(max_length=255, null=True, blank=True)  # Ajustado para varchar
    saldo_receber = models.CharField(max_length=255, null=True, blank=True)  # Ajustado para varchar
    rendimento = models.CharField(max_length=255, null=True, blank=True)  # Ajustado para varchar
    total_realizado = models.CharField(max_length=255, null=True, blank=True)  # Ajustado para varchar
    total_empenhado = models.CharField(max_length=255, null=True, blank=True)  # Ajustado para varchar
    saldo_executar = models.CharField(max_length=255, null=True, blank=True)  # Ajustado para varchar
    data = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        managed = False  # O Django não deve tentar criar ou alterar esta tabela
        db_table = 'dash_nit"."execfinanceira_nit' # Inclui o schema 'dashboards' no nome da tabela

class ExecValoresNit(models.Model):
    id = models.AutoField(primary_key=True)
    convenio = models.CharField(max_length=2000, null=True, blank=True)
    desc_execute = models.CharField(max_length=2000, null=True, blank=True)
    aloc = models.CharField(max_length=50, null=True, blank=True)
    custo = models.CharField(max_length=255, null=True, blank=True)  # Ajustado para varchar
    meta = models.CharField(max_length=255, null=True, blank=True)
    rubrica = models.CharField(max_length=255, null=True, blank=True)
    data = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        managed = False  # O Django não deve tentar criar ou alterar esta tabela
        db_table = 'dash_nit"."execvalores_nit' # Inclui o schema 'dashboards' no nome da tabela

class UsersNit(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        managed = False  # O Django não deve tentar criar ou alterar esta tabela
        db_table = 'dash_nit"."users_nit' # Inclui o schema 'dashboards' no nome da tabela