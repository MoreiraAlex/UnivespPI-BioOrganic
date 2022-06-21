from django.urls import path
from . import views

app_name = 'bio'

urlpatterns = [
    path('', views.home, name='home'),
    path('privacy', views.privacy, name='privacy'),
    path('manun', views.manun, name='manutenção'),
]