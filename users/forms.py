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
            'CEP',
            'Estado',
            'Cidade',
            'Bairro',
            'Endereço',
            'Numero',
            'Complemento',
            'Telefone',
            'Instagram',
            'Realiza descarte de óleo frequentemente?',
            'Se sim, a cada quanto tempo?',
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
        self.fields['Estado'].widget.attrs.update({'disabled': ''})    
        self.fields['Cidade'].widget.attrs.update({'disabled': ''})    
        self.fields['Bairro'].widget.attrs.update({'disabled': ''})    
        self.fields['Endereço'].widget.attrs.update({'disabled': ''})    
        self.fields['Numero'].widget.attrs.update({'disabled': ''})    
        self.fields['Complemento'].widget.attrs.update({'disabled': ''})    
        self.fields['Telefone'].widget.attrs.update({'disabled': ''})    
        self.fields['Instagram'].widget.attrs.update({'disabled': ''})    
        self.fields['Realiza descarte de óleo frequentemente?'].widget.attrs.update({'disabled': ''})    
        self.fields['Se sim, a cada quanto tempo?'].widget.attrs.update({'disabled': ''})    
        self.fields['CEP'].widget.attrs.update({'disabled': ''})