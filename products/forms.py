from django import forms
from .models import Products

class ProductsCreateForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('product','tradermark','presentation','price','description','serial_number',
                  'state', 'category')
        exclude = ['create_date', 'update_date','create_by','update_by']
        widgets = {
            'product':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Producto'
            }),'tradermark':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Marca'
            }),'presentation':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Presentacion'
            }),'price':forms.NumberInput(attrs={
                'class':'form-control',
                'step': '0.01'
            }),'description':forms.Textarea(attrs={
                'class':'form-control',
            }),'serial_number':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Numero serial'
            }),'state':forms.Select(attrs={
                'class':'form-control',
            }, choices=[(True, 'Disponible'), (False, 'Desactivado')]),
            'category':forms.Select(attrs={
                'class':'form-control',
            })
        }
        labels = {
            'product':'',
            'tradermark':'',
            'presentation':'',
            'price':'',
            'description':'Descripcion',
            'serial_number':'',
            'state':'Estado',
            'category':'Categoria'
        }
        