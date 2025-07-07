from django.shortcuts import render
from .models import Barbeiro

def home(request):
    return render(request, 'core/home.html')

def sobre(request):
    return render(request, 'core/sobre.html')

def contactos(request):
    barbeiros = Barbeiro.objects.all()
    return render(request, 'core/contactos.html', {'barbeiros': barbeiros})
