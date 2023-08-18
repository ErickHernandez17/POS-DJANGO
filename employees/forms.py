from django import forms
from .models import  Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserFormCreation(UserCreationForm):
    model = User
    fields = ('username','password1','password2')
    widgets = {
        'username':forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Usuario'
        }),
        'password1':forms.PasswordInput(attrs={
            'class':'form-control'
        }),
        'password2': forms.PasswordInput(attrs={
            'class': 'form-control'
        })
    }
    labels = {
        'username':'',
        'password1':'',
        'password2': ''
    }


class EmployeeFormCreation(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name','last_name','rfc','curp']
        exclude = ['user', 'address']
        widgets = {
            'first_name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Nombres'
            }),
            'last_name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Apellidos'
            }),
            'rfc':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'RFC'
            }),
            'curp':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'CURP'
            }),
        }
        labels = {
            'first_name':'',
            'last_name':'',
            'rfc':'',
            'curp':'',
        }
        
        
class ChangePass(forms.ModelForm):
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    
    