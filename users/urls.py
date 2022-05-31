from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('data/<int:id>/', views.view_data, name='data'),
    path('data-edit/<int:id>/', views.edit_data, name='data-edit'),
]