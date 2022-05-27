from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def manun(request):
    return render(request, 'manutencao.html')