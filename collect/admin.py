from django.contrib import admin
from .models import Collect

# Register your models here.
admin.site.register(Collect)
'''@admin.register(Collect)
class CollectAdmin(admin.UserAdmin):
    model = Collect
    
    fieldsets = (
        ('Contato', {'fields': ('phone', 'insta',)}),
        ('Endereço', {'fields': ('cep', 'uf', 'city', 'block', 'address', 'number', 'complement',)}),
        ('Descarte', {'fields': ('descard', 'time',)}),
        ('Cadastro', {'fields': ('full',)}),
    )

    list_display = ('username', 'email', 'first_name', 'is_active', 'is_staff')'''

