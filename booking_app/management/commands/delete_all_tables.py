from django.core.management.base import BaseCommand
from booking_app.models import Table

class Command(BaseCommand):
    help = 'Deletes all tables'

    def handle(self, *args, **kwargs):
        Table.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all tables'))
