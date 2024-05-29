from django.contrib import admin

# Register your models here.

from .models import Convenio, Meta, Fp_nit, Atividade, Andamento, Cargo, Empregado, Cargo_Empregado, Contrato, Exec_Financeira, Exec_Valores, Evento, Convenio_Empregado

admin.site.register(Convenio)
admin.site.register(Meta)
admin.site.register(Fp_nit)
admin.site.register(Atividade)
admin.site.register(Andamento)
admin.site.register(Cargo)
admin.site.register(Empregado)
admin.site.register(Cargo_Empregado)
admin.site.register(Contrato)
admin.site.register(Exec_Financeira)
admin.site.register(Exec_Valores)
admin.site.register(Evento)
admin.site.register(Convenio_Empregado)