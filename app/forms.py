from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    Username=forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    password=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))


class CustomerRegistrationForm(UserCreationForm):
    Username=forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    email=forms.EmailField()
    password1=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

class Meta:
    model = User
    fields = ['Username','email','password1',' password2']
    
