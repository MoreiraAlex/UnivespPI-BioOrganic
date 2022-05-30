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

class Full_signup(forms.ModelForm):
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
