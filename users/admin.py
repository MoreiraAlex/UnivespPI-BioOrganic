from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import CustomUser

admin.site.register(CustomUser, auth_admin.UserAdmin)
