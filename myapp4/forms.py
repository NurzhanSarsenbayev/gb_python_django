from django import forms
import datetime

class UserForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    age = forms.IntegerField(min_value=1, max_value=120, label='Age')


class ManyFieldsForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    age = forms.IntegerField(min_value=1, max_value=120, label='Age')
    height = forms.FloatField()
    is_active = forms.BooleanField()
    birthdate = forms.DateField(initial=datetime.date.today)
    gender = forms.ChoiceField(choices=(('M', 'Male'), ('F', 'Female'),))

class ManyFieldsFormWidget(forms.Form):
    name = forms.CharField(label='Name', max_length=100,
                           widget = forms.TextInput(attrs={'class': 'form-control',
                                                     'placeholder': 'Name'}))
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'user@email.ru'}))
    age = forms.IntegerField(min_value=1, max_value=120, label='Age',
                             widget=forms.NumberInput(attrs={'class': 'form-control',}))
    height = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}))
    is_active = forms.BooleanField(required=False,
                                   widget=forms.CheckboxInput(attrs={'class': 'form-control',}))
    birthdate = forms.DateField(initial=datetime.date.today,
                                widget=forms.DateInput(attrs={'class': 'form-control',
                                                              'type': 'date'}))
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')],
                               widget=forms.RadioSelect(attrs={'class': 'form-check-input',}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',}))

class UserForm2(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    age = forms.IntegerField(min_value=1, max_value=120, label='Age')

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) <3 :
            raise forms.ValidationError('Name must be at least 3 characters')
        return name

    def clean_email(self):
        email:  str = self.cleaned_data['email']
        if not (email.endswith('@gmail.com')) or email.endswith('@mail.ru'):
            raise forms.ValidationError('Email must end with @gmail.com')
        return email

class ImageForm(forms.Form):
    image = forms.ImageField()
