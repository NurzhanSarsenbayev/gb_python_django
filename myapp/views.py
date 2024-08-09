from django.http import HttpResponse
from django.shortcuts import render
import logging

# Create your views here.

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed')
    return HttpResponse("Hello, world. You're at the polls index.")

def about(request):
    try:
        result = 1/0
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse('Oops, something went wrong')
    else:
        logger.debug('About page accessed')
        return HttpResponse("About")

def anna(request):
    logger.info('Anna page accessed')
    return HttpResponse("Привет Анька. Представь что тут танцует единорог)))")