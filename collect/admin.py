from django.contrib import admin
from .models import Collect

@admin.register(Collect)
class CollectAdmin(admin.ModelAdmin):

    list_display = ('user', 'name', 'status',)
    list_filter = ('user', 'name', 'status', 'date', 'time',)
    search_fields = ('user', 'name', 'status',)

