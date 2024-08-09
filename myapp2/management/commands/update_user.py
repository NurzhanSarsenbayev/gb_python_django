from django.core.management import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = 'Update user name by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='pk of user to update')
        parser.add_argument('name', type=str, help='name of user to update')

    def handle(self, *args, **options):
        pk = options.get('pk')
        name = options.get('name')
        user = User.objects.filter(pk=pk).first()
        user.name = name
        user.save()
        self.stdout.write(f"{user}")