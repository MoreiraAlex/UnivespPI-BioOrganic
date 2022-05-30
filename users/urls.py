from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('data/<int:id>/', views.data, name='data'),
]