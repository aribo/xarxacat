# -*- coding: utf8 -*- 

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Benvingut/da al tauler de la xarxa de l'acció exterior.")