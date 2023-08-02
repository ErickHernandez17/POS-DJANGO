from django import forms
from .models import Countries, Cities, Address

class CountriesForm(forms.ModelForm):
    class Meta:
        model = Countries
        fields = ['country']
        widgets = {
            'country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'País'
            })
        }
        labels = {
            'country': ''
        }
        
        
class CitiesForm(forms.ModelForm):
    class Meta:
        model = Cities
        fields = ['city','country']
        widgets = {
            'city':forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ciudad'
            }),
            'country':forms.Select(attrs={
                'class': 'form-control'
            })
        }
        labels = {
            'city':''
        }
        
        
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address','cp','city']
        widgets = {
            'address':forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Direccion'
            }),
            'cp':forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'city':forms.Select(attrs={
                'class': 'form-control',
            })
        }
        
        