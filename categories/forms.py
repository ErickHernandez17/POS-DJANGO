from django import forms 
from .models import Categories

class CategoryCreateForm(forms.ModelForm):
    
    class Meta:
        model = Categories
        fields = ("category",'state')
        widgets = {
            'category':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Categoria'
            }),
            'state':forms.Select(attrs={
                'class':'form-control',
                
            }, choices=[(True, 'Disponible'), (False, 'Desactivado')])
        }
        labels = {
            'category':'',
            'state':'Estado'
        }
