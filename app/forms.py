from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField ,PasswordChangeForm
from django.contrib.auth.models import User
from .models import Customer

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

class mypasswordResetForm(PasswordChangeForm):
    pass
class CustomerProfileform(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','locality','city','mobile','state','Zipcode']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'Zipcode':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
       }
        

   



    
    
