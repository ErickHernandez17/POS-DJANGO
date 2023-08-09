from django import forms
from .models import Ticket, Items
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['create_by', 'update_by']
        
class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['ticket','product','price','quantity']
        widgets = {
            'ticket':forms.HiddenInput(),
            'product':forms.Select(attrs={
                'class':'form-control'
                }),
            'price': forms.HiddenInput(),
            'quantity':forms.NumberInput(attrs={
                'class':'form-control'
            })
        }
