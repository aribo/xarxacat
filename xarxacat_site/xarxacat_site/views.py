# -*- coding: utf8 -*- 

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Bevingut/da a la xarxa de l'acció exterior. Accés a <a href=\"./admin\">Administració</a>")