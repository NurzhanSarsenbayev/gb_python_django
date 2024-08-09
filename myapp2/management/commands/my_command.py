from django.core.management import BaseCommand

class Command(BaseCommand):
    help = "Print 'Hello World' to output"

    def handle(self, *args, **kwargs):
        self.stdout.write('Hello World')