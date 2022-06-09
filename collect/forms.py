from django import forms
from django.forms import ModelForm

from collect.models import Collect
 

class CollectForm(ModelForm):
    class Meta:
        model = Collect
        fields = [
            'liters',
            'cep',
            'uf',
            'city',
            'block',
            'address',
            'number',
            'complement',
            'date',
            'time',
            'img',
        ]
        exclude = [
            'username',
            'created',
            'status',
            'obs',
            'real_liters',
        ]
           
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  
        self.fields['date'].widget=forms.widgets.DateInput(attrs={'type': 'date'})