import logging

from django.core.files.storage import FileSystemStorage

from .models import User
from django.shortcuts import render
from .forms import UserForm, ManyFieldsForm, ManyFieldsFormWidget, UserForm2, ImageForm

# Create your views here.

logger = logging.getLogger(__name__)

def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']

            logger.info(f'Received {name=}, {email=}, {age=}')

    else:
        form = UserForm()

    return render(request, 'myapp4/basic_form.html', {'form':form})

def many_field_form(request):
    if request.method == 'POST':
        form = ManyFieldsForm(request.POST)
        if form.is_valid():

            logger.info(f'Received {form.cleaned_data=}')

    else:
        form = ManyFieldsForm()
    return render(request, 'myapp4/basic_form.html', {"form":form})


def many_field_form_widget(request):
    if request.method == 'POST':
        form = ManyFieldsFormWidget(request.POST)
        if form.is_valid():

            logger.info(f'Received {form.cleaned_data=}')

    else:
        form = ManyFieldsFormWidget()
    return render(request, 'myapp4/basic_form.html', {"form":form})


def add_user(request):
    if request.method == 'POST':
        form = UserForm2(request.POST)
        message = "Error"
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'Received {name=}, {email=}, {age=}')
            user = User(name=name, email=email, age=age)
            user.save()
            message = "User added"
    else:
        form = UserForm2()
        message = "Fill up the form"
    return render(request, 'myapp4/basic_form.html', {'form':form, 'message':message})

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        message = 'Error'
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            message = "Image uploaded"
    else:
        form = ImageForm()
        message = "Upload the image"
    return render(request, 'myapp4/upload_image.html', {'form':form, 'message':message})