from django.core.management.base import BaseCommand
from myapp2.models import Author,Post

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **options):
        pk = options.get('pk')
        posts = Post.objects.filter(author__pk=pk)
        intro = f'All posts\n'
        text = '\n'.join(post.get_summary() for post in posts)
        self.stdout.write(f'{intro}{text}')