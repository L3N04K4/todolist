from django.core.management.base import BaseCommand
from base.models import *

class Command(BaseCommand):
    help = 'List all users.'

    def handle(self, *args, **options):
        users = User.objects.all()
        for user in users:
            self.stdout.write((f'Username: {user.username}, Email: {user.email}, SuperUser: {user.is_superuser}'))