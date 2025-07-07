from django.shortcuts import render
from .models import Corte

def exemplos(request):
    cortes = Corte.objects.all()
    return render(request, 'cortes/exemplos.html', {'cortes': cortes})
