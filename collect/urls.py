from django.urls import path
from . import views

app_name = 'collect'

urlpatterns = [
    path('info', views.collect, name='info'),
    path('collect', views.collect_create, name='collect')
    #path('data/<int:id>/', views.view_data, name='data'),
]