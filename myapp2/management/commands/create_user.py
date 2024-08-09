from django.core.management.base import BaseCommand
from myapp2.models import User

class Command(BaseCommand):
    help = "Creates new user"

    def handle(self, *args, **options):
        # user = User(name='John', email='john@example.com',password='secret', age=25)
        # user = User(name='Jack', email='jack@example.com', password='secret', age=21)
        # user = User(name='Jill', email='jill@example.com', password='secret', age=32)
        user.save()
        self.stdout.write(f'{user}')

