from gc import collect
from django.shortcuts import render
from users.models import User
from collect.models import Collect 

def home(request):
    users = User.objects.all()
    count_user = User.objects.count()
    count_liters = 0
    count_water = 0

    for i in users:
        collects = Collect.objects.filter(user = i)        

        for j in collects:
            count_liters += j.real_liters

    return render(request, 'home.html', {'users': count_user, 'liters_oil': int(count_liters), 'liters_water': count_water})


def privacy(request):
    return render(request, 'privacy.html')


def manun(request):
    return render(request, 'manutencao.html')