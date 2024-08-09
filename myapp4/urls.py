from django.urls import path
from .views import user_form, many_field_form, many_field_form_widget, add_user, upload_image

urlpatterns = [
    path('user/add/', add_user, name='add_user'),
    path('form/', many_field_form, name='many_field_form'),
    path('form/widget/', many_field_form_widget, name='many_field_form_widget'),
    path('upload/', upload_image, name='upload_image'),
]