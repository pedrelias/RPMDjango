from django.shortcuts import render
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse
from django.views import View
from app.models import *
from app.views import *


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')
    

def f1(request):
    return render(request, 'f1/f1.html')

def indy(request):
    return render(request, 'indy/indy.html')

def nascar(request):
    return render(request, 'nascar/nascar.html')


def f1_view(request):
    f1_categoria = CategoriaAutomobilismo.objects.get(nome='Formula 1')
    corridas_f1 = Corrida.objects.filter(categoria=f1_categoria)
    calendario_f1 = Calendario.objects.filter(corrida__in=corridas_f1)
    equipes_f1 = Equipe.objects.filter(corrida__in=corridas_f1)
    pilotos_f1 = Piloto.objects.filter(equipe__in=equipes_f1)
    
    context = {
        'calendario': calendario_f1,
        'equipes': equipes_f1,
        'pilotos': pilotos_f1,
    }
    
    return render(request, 'f1.html', context)
