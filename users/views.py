from django.shortcuts import render, redirect, get_object_or_404

from .forms import DataForm, Full_signup
from .models import User

def profile(request):
    return render(request, 'account/profile.html')


def view_data(request, id):
    user = get_object_or_404(User, pk=id)
    form = DataForm(instance=user)

    if request.method == 'POST':
        return False
    else:
        return render(request, 'account/data.html', {'form': form})


def edit_data(request, id):
    user = get_object_or_404(User, pk=id)
    form = Full_signup(instance=user)

    if request.method == 'POST':
        form = Full_signup(request.POST, instance=user)

        if form.is_valid():
            user.Completo = True
            user.save()
            return redirect('/accounts/data/' + str(id))
        else:
            return render(request, 'account/data-edit.html', {'form': form})
    else:
        return render(request, 'account/data-edit.html', {'form': form})