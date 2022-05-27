from cProfile import label
from secrets import choice
from tkinter.tix import Select
from unicodedata import name
from allauth.account.forms import SignupForm
from django import forms
 
 
class CustomSignupForm(SignupForm):
    name = forms.CharField(max_length=30, label='Nome completo')
    address = forms.CharField(max_length=50, label='Endereço(Logadouro, numero, bairro, cidade, estado, CEP)')
    descart = forms.NullBooleanField(label='Realiza descarte de óleo frequentemente?',
        widget=forms.RadioSelect(
            choices=[
                (True, 'Sim'),
                (False, 'Não')
            ]
        )
    )
    time = forms.NullBooleanField(label='Se sim, a cada quanto tempo?',
        widget=forms.RadioSelect(
            choices=[
                (False, 'Não descarto'),
                ('Duas semanas', 'A cada duas semanas'),
                ('Um mês', 'A cada um mês'),
                ('Dois meses', 'A cada dois meses')
            ]
        )
    )

    def signup(self, request, user):
        user.name = self.cleaned_data['first_name']
        user.descart = self.cleaned_data['descart']
        user.time = self.cleaned_data['time']
        user.save()
        return user