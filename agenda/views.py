from django.shortcuts import render
from django.http import HttpResponse
from agenda.models import *

# Create your views here.

def listaAgendas(request):
    
    retorno = "<h1> Todas as agendas </h1>"
    listaAgendas = Agenda.objects.all()
    for agenda in listaAgendas:
        retorno += '<br> Nome da agenda: {}<br> '.format(agenda.nome_Da_Agenda)
    return HttpResponse(retorno)

