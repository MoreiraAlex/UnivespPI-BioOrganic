from django.urls import path
from . import views

app_name = 'collect'

urlpatterns = [
    path('', views.collect, name='collect'),
    #path('data/<int:id>/', views.view_data, name='data'),
]