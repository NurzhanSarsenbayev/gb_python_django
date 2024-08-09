from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import TemplateView

from .models import Author,Post
# Create your views here.


def hello(request):
    return HttpResponse("Hello World from function!")

class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello World from class!")

def year_post(request, year):
    text = ''
    ...
    return HttpResponse(f'Posts from {year}<br>{text}')

class MonthPost(View):
    def get(self, request, year, month):
       text = ''
       ...
       return HttpResponse(f'Posts from {month}/{year}<br>{text}')

def post_detail(request, year, month, slug):
    ...
    post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "What is faster: list() or []",
        "content": "I had this thought during my work, "
                   "which was the most optimal way to create lists in Python"
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})

def my_view(request):
    context = {
        "name": "Nurzhan"
    }
    return render(request, "myapp3/my_template.html", context)

class TemplateIf(TemplateView):
    template_name = 'myapp3/if_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Hello World from template"
        context['number'] = 5
        return context
def view_for(request):
    my_list = [1, 2, 3, 4, 5]
    my_dict = {
        "hello1": "world",
        "hello2": "world",
        "hello3": "world",
        "hello4": "world",
    }

    context = {
        "my_list": my_list,
        "my_dict": my_dict
    }

    return render(request, "myapp3/for_template.html", context)

def index(request):
    return render(request, "myapp3/index.html")
def about(request):
    return render(request, "myapp3/about.html")

def author_post(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 'myapp3/author_posts.html', {"author": author, "posts": posts})

def post_full(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'myapp3/post_full.html', {"post": post})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'myapp3/author_list.html', {"authors": authors})