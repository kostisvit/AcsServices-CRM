from .models import *
import datetime

def ergasies_count(request):
    today = datetime.date.today()
    return { 'total_ergasies' : Ergasies.objects.filter(importdate__year=today.year).count() }


def training_count(request):
    today = datetime.date.today()
    return { 'total_training': Training.objects.filter(importdate__year=today.year).count()}

# Σύνολο αιτημάτων προς την  ACS
def aithmata_count_all(request):
    today = datetime.date.today()
    return { 'all_aithmata': Aithmata.objects.filter(importdate__year=today.year).count()}

# Σύνολο αιτημάτων προς υπάλληλο ACS
def aithmata_count(request):
    today = datetime.date.today()
    return { 'total_aithmata' : Aithmata.objects.filter(importdate__year=today.year,assign=request.user).order_by('-importdate').count() }
        