from django.shortcuts import render, get_object_or_404, redirect
from .forms import CollectForm
from .models import Collect
from users.models import User


def collect(request):
    users = User.objects.filter(username = request.user)
    form = CollectForm()

    for i in users:
        user = i

    collections = Collect.objects.all().filter(user = user).order_by('-created')

    oilLiters = 0
    for i in collections:
        if i.status == 'Concluida':
            oilLiters += i.real_liters

    if request.method == 'POST':
        form = CollectForm(request.POST, request.FILES)

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


def collectDetails(request, id):
    collect = get_object_or_404(Collect, pk=id)
    form = CollectForm(instance=collect)

    if request.method == 'POST':
        form = CollectForm(request.POST, request.FILES, instance=collect)
 
        if form.is_valid():
            form.save()
            return redirect('/collect/' + str(id))
        else:
            return render(request, 'collect/collect_details.html', {'form': form, 'collect': collect})

    else:
        return render(request, 'collect/collect_details.html', {'form': form, 'collect': collect})

def collectCancel(request, id):
    collect = get_object_or_404(Collect, pk=id)
    print('entrou')
    collect.status = 'Cancelada'
    collect.save()
    return redirect('/collect/' + str(id))