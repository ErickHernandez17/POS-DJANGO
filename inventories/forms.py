from django import forms
from .models import Inventories
class InvetoriesForm(forms.ModelForm):
    class Meta:
        models = Inventories