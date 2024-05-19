from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from app.models import Koment,Submodal


class Register(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ModalKom (forms.ModelForm):
    class Meta:
        model = Koment
        fields = ['content', 'rating']


class SupportForm(ModelForm):
     class Meta:
         model=Submodal
         fields = ['name','email','message']

