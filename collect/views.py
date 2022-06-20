from django.shortcuts import render, get_object_or_404, redirect
from .forms import CollectForm
from .models import Collect
from users.models import User


def collect(request):
    form = CollectForm()

    collections = Collect.objects.all().filter(user = request.user).order_by('-id')

    oilLiters = 0
    for i in collections:
        if i.status == 'Concluida':
            oilLiters += i.real_liters

    if request.method == 'POST':
        form = CollectForm(request.POST, request.FILES)

        if form.is_valid():
            users = User.objects.filter(username = request.user)
            
            collect = form.save(commit=False)
            collect.user = users[0]
            collect.name = users[0].first_name + ' ' + users[0].last_name
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
    collect.status = 'Cancelada'
    collect.save()
    return redirect('/collect/' + str(id))