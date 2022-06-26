from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from users.forms import UserChangeForm
from .models import User

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    
    model = User
    
    fieldsets = (
        (None, {'fields': ('cpf_cnpj',)}),
        ('Contato', {'fields': ('phone', 'insta',)}),
        ('Endereço', {'fields': ('cep', 'uf', 'city', 'block', 'address', 'number', 'complement',)}),
        ('Cadastro', {'fields': ('liters', 'full',)}),
    ) + auth_admin.UserAdmin.fieldsets

    list_display = ('username', 'email', 'first_name', 'is_active', 'is_staff')
    

