from django.contrib.auth.models import User
from django import forms
from .models import Animals
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class AnimalsForm(ModelForm):
    class Meta:
        model=Animals
        fields=['title', 'full_text', 'date']

        widgets={
            'title': TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Название статьи'
            }),
            "full_text": Textarea(attrs={
            'class': 'form-control',
            'placeholder':'Текст статьи'
            }),
            "date": DateTimeInput(attrs={
            'class': 'form-control',
            'placeholder':'Дата статьи'
            }),

        }

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
