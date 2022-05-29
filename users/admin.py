from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from users.forms import UserChangeForm
from .models import User

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    
    model = User
    
    fieldsets = (
        ('Contato', {'fields': ('phone', 'insta',)}),
        ('Endereço', {'fields': ('address',)}),
        ('Descarte', {'fields': ('discard', 'time',)})
    ) + auth_admin.UserAdmin.fieldsets

    list_display = ('username', 'email', 'first_name', 'phone', 'is_active', 'is_staff')
    

