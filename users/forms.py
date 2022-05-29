from cProfile import label
from logging import PlaceHolder
from pyexpat import model
from secrets import choice
from tkinter.tix import Select
from unicodedata import name
from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth import forms as auth_forms
from allauth.account.adapter import get_adapter

from users.models import User
 

class UserChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = User


'''class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='Nome', widget=forms.TextInput(attrs={'placeholder': ('Primeiro nome')}))
    last_name = forms.CharField(max_length=30, label='Sobrenome', widget=forms.TextInput(attrs={'placeholder': ('Ultimo nome')}))
    cep = forms.CharField(max_length=9, label='CEP', widget=forms.TextInput(attrs={'placeholder': ('12345-678')}))
    uf = forms.CharField(label='Estado')
    city = forms.CharField(label='Cidade')
    block = forms.CharField(label='Bairro')
    address = forms.CharField(label='Endereço')
    phone = forms.CharField(max_length='14', label='Celular', widget=forms.TextInput(attrs={'placeholder': ('99 99999-9999')}))
    insta = forms.CharField(max_length=30, label='Instagram', required=False, widget=forms.TextInput(attrs={'placeholder': ('Perfil do Instagram')}))
    discard = forms.NullBooleanField(label='Realiza descarte de óleo frequentemente?',
        widget=forms.Select(
            choices=[
                (True, 'Sim'),
                (False, 'Não')
            ]
        )
    )
    time = forms.NullBooleanField(label='Se sim, a cada quanto tempo?',
        widget=forms.Select(
            choices=[
                (False, 'Não descarto'),
                ('Duas semanas', 'A cada duas semanas'),
                ('Um mês', 'A cada um mês'),
                ('Dois meses', 'A cada dois meses')
            ]
        )
    )

    def signup(self, request):

        user = super(CustomSignupForm, self).save(request)

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone = self.cleaned_data['phone']
        user.phone = get_adapter().clean_username(user.phone)
        user.insta = self.cleaned_data['insta']
        user.address = self.cleaned_data['address']
        user.discard = self.cleaned_data['discard']
        user.time = self.cleaned_data['time']

        user.save()

        return user'''