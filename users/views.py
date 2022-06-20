from django.shortcuts import render, redirect, get_object_or_404

from .forms import DataForm, DataFormEdit
from .models import User

def profile(request, id):
    user = get_object_or_404(User, pk=id)
    return render(request, 'account/profile.html', {'user': user})


def view_data(request, id):
    user = get_object_or_404(User, pk=id)
    form = DataForm(instance=user)

    if request.method == 'POST':
        return False
    else:
        return render(request, 'account/data.html', {'form': form})


def edit_data(request, id):
    user = get_object_or_404(User, pk=id)
    form = DataFormEdit(instance=user)

    if request.method == 'POST':
        form = DataFormEdit(request.POST, instance=user)

        if form.is_valid():
            user.full = True
            user.save()
            return redirect('/accounts/data/' + str(id))
        else:
            return render(request, 'account/data-edit.html', {'form': form})
    else:
        return render(request, 'account/data-edit.html', {'form': form})