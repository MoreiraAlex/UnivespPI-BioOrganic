from django.shortcuts import render, get_object_or_404, redirect
from .forms import CollectForm
from .models import Collect
from users.models import User


def collect(request):
    users = User.objects.filter(username = request.user)
    form = CollectForm()

    for i in users:
        user = i

    collections = Collect.objects.all().order_by('-created').filter(user = user)

    oilLiters = 0
    for i in collections:
        if i.status == 'Aprovada':
            oilLiters += i.liters

    if request.method == 'POST':
        form = CollectForm(request.POST)

        if form.is_valid():
            collect = form.save(commit=False)
            collect.user = user
            collect.name = user.first_name + ' ' + user.last_name
            collect.save()
            return redirect('/collect')
        else:
            return render(request, 'collect/collect.html', {'form': form, 'collections': collections, 'oilLiters': oilLiters})
    else:
        return render(request, 'collect/collect.html', {'form': form, 'collections': collections, 'oilLiters': oilLiters})