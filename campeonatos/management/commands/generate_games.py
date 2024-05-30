# campeonatos/management/commands/generate_games.py

from django.core.management.base import BaseCommand
from campeonatos.utils import generate_games_for_championship

class Command(BaseCommand):
    help = 'Generate games for a championship based on its ID'

    def add_arguments(self, parser):
        parser.add_argument('championship_id', type=int, help='ID of the championship')

    def handle(self, *args, **kwargs):
        championship_id = kwargs['championship_id']
        result = generate_games_for_championship(championship_id)
        self.stdout.write(self.style.SUCCESS(result))
