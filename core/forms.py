

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = {'username','email','password1','password2'}

    username = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder':'Enter your username' , 'class':'w-full px-2 py-3 rounded-xl'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={ 'placeholder':'Enter your email' , 'class':'w-full px-2 py-3 rounded-xl'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={ 'placeholder':'Enter your password' , 'class':'w-full px-2 py-3 rounded-xl'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={ 'placeholder':'Confirm your password' , 'class':'w-full px-2 py-3 rounded-xl'}))

    



