from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AppelOffreForm(ModelForm):
    class Meta:
        model = Appel_Offre
        fields = '__all__'


class PosteForm(ModelForm):
    class Meta:
        model = postulation
        fields = '__all__'
        #exclude = ['titre']


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
