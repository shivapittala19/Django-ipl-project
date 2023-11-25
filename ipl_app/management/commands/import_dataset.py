# import_dataset.py

import csv
from django.core.management.base import BaseCommand
from django.db import transaction
from ...models import Matches, Deliveries

class Command(BaseCommand):
    help = 'Import dataset into Match and Delivery tables using atomic transactions'

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                self.import_matches()
                self.import_deliveries()
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error during data import: {e}'))

    def import_matches(self):
        self.stdout.write(self.style.SUCCESS('Importing matches...'))

        with open('matches.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row.pop('id')
                Matches.objects.create(**row)
                
        self.stdout.write(self.style.SUCCESS('Matches imported successfully.'))

    def import_deliveries(self):
        self.stdout.write(self.style.SUCCESS('Importing deliveries...'))

        with open('deliveries.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                match_id_id = row.pop('match_id')
                match_id = Matches.objects.get(id=match_id_id)
                Deliveries.objects.create(match_id=match_id, **row)
        self.stdout.write(self.style.SUCCESS('Deliveries imported successfully.'))
