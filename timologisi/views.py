from django.shortcuts import render
from timologisi.models import *


def prosfora(request):
    return render(request,'main/prosfora.html')


def symbasi(request):
    return render(request,'main/symbasi.html')


def timologio(request):
    return render(request,'main/timologisi.html')
