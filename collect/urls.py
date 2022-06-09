from django.urls import path
from . import views

app_name = 'collect'

urlpatterns = [
    path('', views.collect, name='collect'),
    path('<int:id>', views.collectDetails, name='collectDetails'),
    path('cancel/<int:id>', views.collectCancel, name='collectCancel'),
]