from django.core.management.base import BaseCommand
from myapp2.models import Author,Post

class Command(BaseCommand):
    help = 'Create fake data for authors and posts'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='user id')

    def handle(self, *args, **options):
        count = options.get('count')
        for i in range(1, count+1):
            author = Author(name=f'Name{i}', email=f'mail{i}@example.com')
            author.save()
            for j in range(1, count+1):
                post = Post(
                    title=f'Title{j}',
                    content=f'Text from {author.name} is bla bla bla many long text',
                    author=author,
                )
                post.save()