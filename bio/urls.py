from django.urls import path
from . import views

app_name = 'bio'

urlpatterns = [
    path('', views.home, name='home'),
    path('privacy', views.privacy, name='privacy'),
    path('contents', views.contents, name='contents'),
    path('patners', views.patners, name='patners'),
    path('manun', views.manun, name='manutenção'),
]