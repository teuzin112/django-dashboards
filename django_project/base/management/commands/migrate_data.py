from django.core.management.base import BaseCommand
from legacy.models import AtvMetas as LegacyAtvMetas
from base.models import Convenio, Meta, Atividade
from datetime import datetime

class Command(BaseCommand):
    help = 'Migrate data from legacy database to new database'

    def handle(self, *args, **kwargs):
        legacy_data = LegacyAtvMetas.objects.using('dashboards_old').all()
        for item in legacy_data:
            # Criar ou obter o Convenio
            convenio, created = Convenio.objects.get_or_create(
                codigo=item.convenio,
                defaults={
                    'nome': 'Nome padrão',  # Altere conforme necessário
                    'data_inicio': '2022-01-01',  # Altere conforme necessário
                    'data_final': '2022-12-31',  # Altere conforme necessário
                    'orcamento': 0.0  # Altere conforme necessário
                }
            )

            # Criar ou obter a Meta
            meta, created = Meta.objects.get_or_create(
                convenio=convenio,
                nome=item.meta,
                defaults={
                    'data_inicio': self.convert_date_format(item.begin_date),
                    'data_final': self.convert_date_format(item.end_date)
                }
            )

            # Criar a Atividade
            Atividade.objects.create(
                meta=meta,
                nome=item.atividade,
                data_inicio=self.convert_date_format(item.begin_date),
                data_final=self.convert_date_format(item.end_date)
            )

        self.stdout.write(self.style.SUCCESS('Data migration complete'))

    def convert_date_format(self, date_str):
        try:
            # Converte a data do formato DD/MM/YYYY para YYYY-MM-DD
            return datetime.strptime(date_str, '%d/%m/%Y').strftime('%Y-%m-%d')
        except ValueError:
            # Se a data estiver em um formato inesperado, retorne None ou lidere de outra forma
            return None