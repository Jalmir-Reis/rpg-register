from django.shortcuts import render
from .models import Registro
from .forms import RegistroForm
from django.http import HttpResponseRedirect
from django.contrib import messages
import random

def Atributo():
    atributos = []
    for i in range(6):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        d3 = random.randint(1, 6)
        atributo = d1 + d2 + d3 + 2
        if atributo <= 7:
            atributo = 8
        elif atributo > 18:
            atributo = 18
        atributos.append(atributo)
    return atributos


def home(request):
    List_Atrib = Atributo()
    form = RegistroForm(request.POST or None)
    if form.is_valid():
        envio = form.save(commit=False)
        envio.Atributos = List_Atrib
        envio.save()
        messages.success(request, 'Registrado com sucesso')
        return HttpResponseRedirect('/')
    context = {
        'form':form
    }

    return render(request, 'home.html', context)

def lista_all(request):
    context = {'data_read': Registro.objects.all()}
    return render(request, 'lista_all.html', context)