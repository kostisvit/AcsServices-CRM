from .models import *
import datetime

def ergasies_count(request):
    today = datetime.date.today()
    return { 'total_ergasies' : Ergasies.objects.filter(importdate__year=today.year).count() }


def training_count(request):
    today = datetime.date.today()
    return { 'total_training': Training.objects.filter(importdate__year=today.year).count()}