from django.urls import path
from .views import hello,HelloView
from .views import year_post, MonthPost, post_detail,my_view, TemplateIf
from .views import view_for,index,about
from .views import author_post, post_full,author_list

urlpatterns = [
    path('hello/',hello, name='hello'),
    path('hello2/', HelloView.as_view(), name='hello2'),
    path('posts/<int:year>/', year_post, name='year_post'),
    path('posts/<int:year>/<int:month>', MonthPost.as_view(), name = 'month_post'),
    path('posts/<int:year>/<int:month>/<slug:slug>', post_detail, name='post_detail'),
    path('template/', my_view, name='my_view'),
    path('template/if', TemplateIf.as_view(), name='if_template'),
    path('template/for', view_for, name='view_for'),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('author/<int:author_id>', author_post, name='author_post'),
    path('post/<int:post_id>', post_full, name='post_full'),
    path('authors/', author_list, name='author_list'),
]