from django.core.management.base import BaseCommand
from legacy.models import (AtvMetasNit, AndAtividadesNit, FpsNit, EmployeesNit, EventosNit, ExecFinanceiraNit, ExecValoresNit, UsersNit)
from base.models import Convenio, Meta, Atividade, Andamento, Empregado, Cargo, Cargo_Empregado, Evento, Exec_Financeira, Exec_Valores, Convenio_Empregado, Fp_nit, Contrato
from datetime import datetime

class Command(BaseCommand):
    help = 'Migrate data from legacy database to new database'

    def handle(self, *args, **kwargs):
        self.migrate_atv_metas_nit()
        self.migrate_fps_nit()
        self.migrate_and_atividades_nit()
        self.migrate_employees()
        self.migrate_eventos()
        self.migrate_execfinanceira()
        self.migrate_execvalores()
        self.stdout.write(self.style.SUCCESS('Data migration complete'))

    def convert_date_format(self, date_str):
        try:
            # Converte a data do formato DD/MM/YYYY para YYYY-MM-DD
            return datetime.strptime(date_str, '%d/%m/%Y').strftime('%Y-%m-%d')
        except ValueError:
            # Se a data estiver em um formato inesperado, retorne None ou lidere de outra forma
            return None

    def migrate_atv_metas_nit(self):
        legacy_data = AtvMetasNit.objects.using('dash_nit').all()
        for item in legacy_data:
            convenio, created = Convenio.objects.get_or_create(
                nome='NIT',
                defaults={
                    'codigo': '000',
                    'data_inicio': '2022-01-01',
                    'data_final': '2022-12-31',
                    'orcamento': 0.0
                }
            )
            meta, created = Meta.objects.get_or_create(
                convenio=convenio,
                nome=item.meta,
                defaults={
                    'data_inicio': self.convert_date_format(item.begin_date),
                    'data_final': self.convert_date_format(item.end_date)
                }
            )
            Atividade.objects.create(
                meta=meta,
                nome=item.atividade,
                data_inicio=self.convert_date_format(item.begin_date),
                data_final=self.convert_date_format(item.end_date)
            )

    def migrate_fps_nit(self):
        legacy_data = FpsNit.objects.using('dash_nit').all()
        for item in legacy_data:
            convenio, created = Convenio.objects.get_or_create(
                nome='NIT',
                defaults={
                    'codigo': '000',
                    'data_inicio': '2022-01-01',
                    'data_final': '2022-12-31',
                    'orcamento': 0.0
                }
            )
            meta, created = Meta.objects.get_or_create(
                convenio=convenio,
                nome=item.meta,
                defaults={
                    'data_inicio': self.convert_date_format(item.begin_date),
                    'data_final': self.convert_date_format(item.end_date)
                }
            )

            fp, created = Fp_nit.objecs.get_or_create(
                nome=item.fpname,
                meta=meta,
                defaults={
                    'descricao': '',
                    'data_inicio': self.convert_date_format(item.begin_date),
                    'data_final': self.convert_date_format(item.end_date)
                }
            )
            
            atividade, created = Atividade.objects.get_or_create(
                fp_nit=fp,
                nome=item.atividade,
                defaults={
                    'data_inicio':self.convert_date_format(item.begin_date),
                    'data_final':self.convert_date_format(item.end_date)
                }
            )

    def migrate_and_atividades_nit(self):
        legacy_data = AndAtividadesNit.objects.using('dash_nit').all()
        for item in legacy_data:
            atividade, created = Atividade.objects.get_or_create(
                nome=item.fpatv,
                defaults={
                    'descricao': item.descricao,
                    'link_img': item.link_img,
                    'link_exec': item.link_exec,
                    'data_inicio': self.convert_date_format(item.begin_date),
                    'data_final': self.convert_date_format(item.end_date),
                }
            )
            Andamento.objects.create(
                atividade=atividade,
                porcent_executada=item.perc_and,
                data=self.convert_date_format(item.ult_atual_date)
            )

    def migrate_employees(self):
        legacy_data = EmployeesNit.objects.using('dash_nit').all()
        for item in legacy_data:
            empregado, created = Empregado.objects.get_or_create(
                matricula_cracha=item.username,
                defaults={
                    'nome': item.nome,
                    'cpf': item.cpf,
                    'email': item.email,
                    'data_nascimento': self.convert_date_format(item.nascimento),
                    'genero': item.genero,
                    'telefone': item.telefone,
                    'graduacao': item.graduacao,
                    'username': item.username
                }
            )
            cargo, created = Cargo.objects.get_or_create(
                nome=item.cargo
            )
            cargo_empregado, created = Cargo_Empregado.objects.get_or_create(
                cargo=cargo,
                empregado=empregado,
                defaults={
                'data_inicio_cargo': self.convert_date_format(item.data_contratacao),
                'data_final_cargo': None
                }
            )

            Contrato.objects.create(
                data_contratacao=item.data_contratacao,
                data_vencimento=item.data_venc_contrato,
                cargo_empregado_atual=cargo_empregado,
                empregado=empregado
            )

            Convenio_Empregado.objects.create(
                convenio=item.convenio,
                empregado=empregado,
                atuacao_empregado=item.atuacao_nit,
                data_inicio_atuacao=item.data_contratacao
            )

    def migrate_eventos(self):
        legacy_data = EventosNit.objects.using('dash_nit').all()
        for item in legacy_data:
            convenio, created = Convenio.objects.get_or_create(
                nome=item.convenio,
                defaults={
                    'codigo': '000',
                    'data_inicio': '2022-01-01',
                    'data_final': '2022-12-31',
                    'orcamento': 0.0
                }
            )
            Evento.objects.create(
                convenio=convenio,
                nome=item.den_event,
                descricao=item.desc_evento,
                denominacao=item.den_event,
                participantes=item.part_evento,
                categoria_participantes=item.cat_evento,
                data_inicio=self.convert_date_format(item.date_event),
                data_final=self.convert_date_format(item.date_event)
            )

    def migrate_execfinanceira(self):
        legacy_data = ExecFinanceiraNit.objects.using('dash_nit').all()
        for item in legacy_data:
            convenio, created = Convenio.objects.get_or_create(
                nome=item.convenio,
                defaults={
                    'codigo': '000',
                    'data_inicio': '2022-01-01',
                    'data_final': '2022-12-31',
                    'orcamento': 0.0
                }
            )
            Exec_Financeira.objects.create(
                convenio=convenio,
                orc_total=item.orc_total,
                rep_recebidos=item.rep_recebidos,
                saldo_receber=item.saldo_receber,
                redimento=item.rendimento,
                total_realizado=item.total_realizado,
                total_empenhado=item.total_empenhado,
                saldo_executar=item.saldo_executar,
                data=self.convert_date_format(item.data)
            )

    def migrate_execvalores(self):
        legacy_data = ExecValoresNit.objects.using('dash_nit').all()
        for item in legacy_data:
            convenio, created = Convenio.objects.get_or_create(
                nome=item.convenio,
                defaults={
                    'codigo': '000',
                    'data_inicio': '2022-01-01',
                    'data_final': '2022-12-31',
                    'orcamento': 0.0
                }
            )
            Exec_Valores.objects.create(
                convenio=convenio,
                meta=item.meta,
                desc_execute=item.desc_execute,
                aloc=item.aloc,
                custo=item.custo,
                rubrica=item.rubrica,
                data=self.convert_date_format(item.data)
            )
