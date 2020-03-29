from django.shortcuts import redirect, get_object_or_404
from .models import Dhmos, Employee, Ergasies, Adeia, Aithmata, Polisi, Service, Training, Hardware


def delete_pelatis(request, pk):
    object = Dhmos.objects.get(pk=pk)
    object.delete()
    return redirect('pelatis')


def delete_epafi(request, pk):
    object = Employee.objects.get(pk=pk)
    object.delete()
    return redirect('epafi')


def delete_ergasia(request, pk):
    object = Ergasies.objects.get(pk=pk)
    object.delete()
    return redirect('ergasia')


def delete_adeia(request, pk):
    object = Adeia.objects.get(pk=pk)
    object.delete()
    return redirect('adeia')


def delete_aithma(request, pk):
    object = Aithmata.objects.get(pk=pk)
    object.delete()
    return redirect('aithma')


def delete_polisi(request, pk):
    object = Polisi.objects.get(pk=pk)
    object.delete()
    return redirect('polisi')


def delete_service(request, pk):
    object = Service.objects.get(pk=pk)
    object.delete()
    return redirect('service')


def delete_training(request, pk):
    object = Training.objects.get(pk=pk)
    object.delete()
    return redirect('training')

def delete_hardware(request, pk):
    object = Hardware.objects.get(pk=pk)
    object.delete()
    return redirect('hardware')