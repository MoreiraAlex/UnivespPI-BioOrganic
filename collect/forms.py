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
            'img',
            'date',
        ]
           