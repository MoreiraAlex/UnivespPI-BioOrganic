from django import forms
from django.contrib.auth import forms as auth_forms

from users.models import User
 
class UserChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = User

class DataFormEdit(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'cpf_cnpj',
            'cep',
            'uf',
            'city',
            'block',
            'address',
            'number',
            'complement',
            'liters',
            'phone',
            'insta',
        ]

        exclude = [
            'password',
            'username',
            'email',
            'full',
        ]

class DataForm(forms.ModelForm):
    class Meta():
        model = User

        fields = DataFormEdit().fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  
        self.fields['first_name'].widget.attrs.update({'disabled': ''}) 
        self.fields['last_name'].widget.attrs.update({'disabled': ''})
        self.fields['cpf_cnpj'].widget.attrs.update({'disabled': ''})    
        self.fields['cep'].widget.attrs.update({'disabled': ''})
        self.fields['uf'].widget.attrs.update({'disabled': ''})    
        self.fields['city'].widget.attrs.update({'disabled': ''})    
        self.fields['block'].widget.attrs.update({'disabled': ''})    
        self.fields['address'].widget.attrs.update({'disabled': ''})    
        self.fields['number'].widget.attrs.update({'disabled': ''})    
        self.fields['complement'].widget.attrs.update({'disabled': ''})    
        self.fields['liters'].widget.attrs.update({'disabled': ''})  
        self.fields['phone'].widget.attrs.update({'disabled': ''})    
        self.fields['insta'].widget.attrs.update({'disabled': ''})    