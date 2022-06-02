from django.shortcuts import render, get_object_or_404, redirect
from .forms import CollectForm
from .models import Collect

def collect(request):
    return render(request, 'collect/info.html')


def collect_create(request):
    form = CollectForm()

    if request.method == 'POST':
        form = CollectForm(request.POST)

        if form.is_valid():
            form.save()
            print('validou')
            return redirect('/collect/collect')
        else:
            print('nao validou')
            return render(request, 'collect/view.html')
    else:
        collections = Collect.objects.all()
        return render(request, 'collect/view.html', {'form': form, 'collections': collections})