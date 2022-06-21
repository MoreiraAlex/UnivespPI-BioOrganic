from django.contrib import admin
from .models import Collect
from django.utils.html import format_html
    

@admin.register(Collect)
class CollectAdmin(admin.ModelAdmin):
    def foto(self, obj):
        return format_html(f"<img src='{obj.img.url}' width='500px'/>")

    readonly_fields = ['foto']

    list_display = ('id', 'user', 'name', 'status',)
    list_filter = ('user', 'name', 'status', 'date', 'time',)
    search_fields = ('id', 'user', 'name', 'status',)

    fieldsets = (
        ('Usuario', {'fields': ('user', 'name',)}),
        ('Qualidade da coleta', {'fields': ('liters', 'foto',)}),
        ('Informações sobre a coleta', {'fields': ('cep', 'address', 'number', 'complement', 'block', 'city', 'uf',)}),
        ('', {'fields': ('date', 'time',)}),
        ('Retorno', {'fields': ('real_liters', 'status', 'obs',)}),
    )