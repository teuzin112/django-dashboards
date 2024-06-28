from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db import models, IntegrityError
from django.db.models import Q
from django.db.models.constraints import CheckConstraint

from django.db import models

class Convenio(models.Model):
    codigo = models.CharField(max_length=255)
    nome = models.CharField(max_length=2000)
    descricao = models.TextField(null=True, blank=True)
    data_inicio = models.DateField()
    data_final = models.DateField()
    orcamento = models.FloatField()

    def __str__(self):
        return f"{self.nome}"
    
    class Meta:
        verbose_name_plural = "Convenio"

class Evento(models.Model):
    convenio = models.ForeignKey(Convenio, on_delete=models.CASCADE)
    nome = models.CharField(max_length=2000)
    descricao = models.TextField(null=True, blank=True)
    denominacao = models.CharField(max_length=2000, null=True, blank=True)
    participantes = models.CharField(max_length=2000, null=True, blank=True)
    categoria_participantes = models.CharField(max_length=2000, null=True, blank=True)
    data_inicio = models.DateField()
    data_final = models.DateField()

    def __str__(self):
        return f"{self.nome}"
    
    class Meta:
        verbose_name_plural = "Evento"

class Meta(models.Model):
    convenio = models.ForeignKey(Convenio, on_delete=models.CASCADE)
    nome = models.CharField(max_length=2000)
    descricao = models.TextField(null=True, blank=True)
    data_inicio = models.DateField()
    data_final = models.DateField()

    def __str__(self):
        return f"{self.nome}"
    
    class Meta:
        verbose_name_plural = "Meta"


class Fp_nit(models.Model):
    meta = models.ForeignKey(Meta, on_delete=models.CASCADE)
    nome = models.CharField(max_length=2000)
    descricao = models.TextField(null=True, blank=True)
    data_inicio = models.DateField()
    data_final = models.DateField()

    def __str__(self):
        return f"{'FP ' if 'FP' not in self.nome else ''} {self.nome}"
    
    class Meta:
        verbose_name_plural = "Fp_nit"

class Atividade(models.Model):
    PESOS = {
        1: "1",
        3: "3",
        6: "6"
    }

    meta = models.OneToOneField(Meta, null=True, blank=True, on_delete=models.CASCADE)
    fp_nit = models.OneToOneField(Fp_nit, null=True, blank=True, on_delete=models.CASCADE)
    nome = models.CharField(max_length=2000)
    descricao = models.TextField(null=True, blank=True)
    link_img = models.CharField(max_length=4000, null=True, blank=True)
    link_exec = models.CharField(max_length=4000, null=True, blank=True)
    peso = models.IntegerField(choices=PESOS, null=True, blank=True)
    data_inicio = models.DateField()
    data_final = models.DateField()
    indicador = models.CharField(max_length=20000, null=True, blank=True)

    def __str__(self):
        if self.meta:
            return f"Meta {self.meta.nome} - {self.nome}"
        return f"{self.fp_nit.nome} - {self.nome})"

    class Meta:
        verbose_name_plural = "Atividade"
        constraints = [
            CheckConstraint(
                check=(
                    (Q(meta__isnull=False) & Q(fp_nit__isnull=True)) |
                    (Q(meta__isnull=True) & Q(fp_nit__isnull=False))
                ),
                name='check_atividade_fields'
            )
        ]
    
    def save(self, *args, **kwargs):
        if self.meta and self.fp_nit:
            raise IntegrityError("Uma atividade não pode ter os campos 'meta' e 'fp_nit' preenchidos.")
        super().save(*args, **kwargs)

class Andamento(models.Model):
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    porcent_executada = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{str(self.atividade)} ({self.porcent_executada}%)"
    
    class Meta:
        verbose_name_plural = "Andamento"
    
class Cargo(models.Model):
    nome = models.CharField(max_length=2000)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome}"
    
    class Meta:
        verbose_name_plural = "Cargo"

class Empregado(models.Model):
    GENEROS = {
        "Homem": "Homem",
        "Mulher": "Mulher",
        "Outro": "Outro"
    }

    matricula_cracha = models.CharField(max_length=255)
    nome = models.CharField(max_length=2000)
    cpf = models.CharField(max_length=15)
    email = models.CharField(max_length=255, null=True, blank=True)
    data_nascimento = models.DateField()
    genero = models.CharField(choices=GENEROS, max_length=255)
    telefone = models.CharField(max_length=255, null=True, blank=True)
    graduacao = models.CharField(max_length=255)
    username = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.nome}"
    
    class Meta:
        verbose_name_plural = "Empregado"

class Cargo_Empregado(models.Model):
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    empregado = models.ForeignKey(Empregado, on_delete=models.CASCADE)
    data_inicio_cargo = models.DateField()
    data_final_cargo = models.DateField(null=True, blank=True)    # Se for null então é o cargo atual do 
    
    def __str__(self):
        return f"{self.empregado.nome} ({self.cargo.nome}) {'[Atual]' if self.data_final_cargo is None else ''}"
    
    class Meta:
        verbose_name_plural = "Cargo_Empregado"


class Contrato(models.Model):
    cargo_empregado = models.ForeignKey(Cargo_Empregado, on_delete=models.CASCADE)
    empregado = models.ForeignKey(Empregado, on_delete=models.CASCADE)
    data_contratacao = models.DateField()
    data_vencimento = models.DateField()

    def __str__(self):
        return str(self.cargo_empregado)
    
    class Meta:
        verbose_name_plural = "Contrato"

class Convenio_Empregado(models.Model):
    convenio = models.ForeignKey(Convenio, on_delete=models.CASCADE)
    empregado = models.ForeignKey(Empregado, on_delete=models.CASCADE)
    atuacao_empregado = models.CharField(max_length=255)
    data_inicio_atuacao = models.DateField()
    data_final_atuacao = models.DateField()

    def __str__(self):
        return f"{self.empregado.nome} - {self.atuacao_empregado} ({self.convenio.nome})"
    
    class Meta:
        verbose_name_plural = "Convenio_Empregado"

class Exec_Financeira(models.Model):
    convenio = models.ForeignKey(Convenio, on_delete=models.CASCADE)
    orc_total = models.FloatField(null=True, blank=True)
    rep_recebidos = models.FloatField(null=True, blank=True)
    saldo_receber = models.FloatField(null=True, blank=True)
    redimento = models.FloatField(null=True, blank=True)
    total_realizado = models.FloatField(null=True, blank=True)
    total_empenhado = models.FloatField(null=True, blank=True)
    saldo_executar = models.FloatField(null=True, blank=True)
    data = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Exec Financeira - {self.convenio.nome}"
    
    class Meta:
        verbose_name_plural = "Exec_Financeira"

class Exec_Valores(models.Model):
    convenio = models.ForeignKey(Convenio, on_delete=models.CASCADE)
    meta = models.CharField(max_length=255)
    desc_execute = models.TextField(null=True, blank=True)
    aloc = models.CharField(max_length=50, null=True, blank=True)
    custo = models.FloatField(null=True, blank=True)
    rubrica = models.CharField(max_length=255, null=True, blank=True)
    data = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Exec Valores - {self.convenio.nome}"
    
    class Meta:
        verbose_name_plural = "Exec_Valores"