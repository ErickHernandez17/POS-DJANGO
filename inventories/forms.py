from django import forms
from .models import Inventories
class InvetoriesForm(forms.ModelForm):
    class Meta:
        model = Inventories
        fields = ['product','quantity','state']
        exclude = ['create_date', 'update_date','create_by','update_by']
        widgets = {
            'product':forms.Select(attrs={
                'class':'form-control',
            }),'quantity':forms.NumberInput(attrs={
                'class':'form-control',
                'step': '1'
            }),'state':forms.Select(attrs={
                'class':'form-control',
            }, choices=[(True, 'Disponible'), (False, 'Desactivado')]),
        }
        labels = {
            'state':'Estado'
        }