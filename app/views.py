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
    equipes = Equipe.objects.all()
    pilotos = Piloto.objects.all()

    context = {
        'calendario': calendario_f1,
        'equipes': equipes,
        'pilotos': pilotos,
    }

    return render(request, 'f1/f1.html', context)

def nascar_view(request):
    nascar_categoria = CategoriaAutomobilismo.objects.get(nome='NASCAR')
    corridas_nascar = Corrida.objects.filter(categoria=nascar_categoria)
    calendario_nascar = Calendario.objects.filter(corrida__in=corridas_nascar)
    equipes = Equipe.objects.all()
    pilotos = Piloto.objects.all()

    context = {
        'calendario': calendario_nascar,
        'equipes': equipes,
        'pilotos': pilotos,
    }

    return render(request, 'nascar/nascar.html', context)

def indy_view(request):
    indy_categoria = CategoriaAutomobilismo.objects.get(nome='IndyCar')
    corridas_indy = Corrida.objects.filter(categoria=indy_categoria)
    calendario_indy = Calendario.objects.filter(corrida__in=corridas_indy)
    equipes = Equipe.objects.all()
    pilotos = Piloto.objects.all()

    context = {
        'calendario': calendario_indy,
        'equipes': equipes,
        'pilotos': pilotos,
    }

    return render(request, 'indy/indy.html', context)