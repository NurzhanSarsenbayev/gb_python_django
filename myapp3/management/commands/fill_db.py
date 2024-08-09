from random import choices

from django.core.management.base import BaseCommand
from myapp3.models import Author, Post

LOREM = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam lectus risus, finibus ornare vestibulum et, feugiat quis dui. Vivamus sit amet dolor et magna facilisis rhoncus. Curabitur maximus est sed porta scelerisque. Sed suscipit, arcu volutpat feugiat posuere, eros nisi tristique nibh, mollis vehicula lectus tortor eu purus. Donec ut tortor blandit, sagittis diam eget, suscipit eros. Quisque at magna neque. Nulla faucibus mi at nunc mattis placerat. Pellentesque quis augue quis elit tristique auctor. Integer varius est orci, vel egestas felis dictum nec. Phasellus porta ex sit amet turpis finibus, sed vestibulum nisl efficitur. Praesent ultrices diam enim. In ut tellus sed sem placerat sollicitudin. Donec quis mollis dolor. Etiam viverra, arcu cursus porttitor porttitor, diam nunc auctor nisl, quis placerat magna erat et odio. Phasellus feugiat turpis quis mollis lacinia. Sed ac orci et nisi venenatis pharetra ac non arcu.'


class Command(BaseCommand):
    help = 'Generate fake authors and posts'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int,help='Number of posts to generate')

    def handle(self, *args, **options):
        text = LOREM.split()
        count = options['count']
        for i in range(1, count + 1):
            author = Author(name=f'Author_{i}', email=f'mail{i}@example.com')
            author.save()
            for j in range(1, count+1):
                post = Post(
                    title = f'Title {j}',
                    content = " ".join(choices(text, k=64)),
                    author= author
                )
                post.save()