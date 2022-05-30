from django.shortcuts import render, redirect, get_object_or_404

from .forms import Full_signup
from .models import User

def profile(request):
    return render(request, 'account/profile.html')


def data(request, id):
    user = get_object_or_404(User, pk=id)
    form = Full_signup(instance=user)

    if request.method == 'POST':
        form = Full_signup(request.POST, instance=user)

        if form.is_valid():
            user.save()
            return render(request, 'account/data.html', {'form': form})
        else:
            return render(request, 'account/data.html', {'form': form})
    else:
        return render(request, 'account/data.html', {'form': form})