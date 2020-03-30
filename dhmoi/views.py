from django.shortcuts import render
from django.contrib.auth.models import User
from .filters import PelatisFilter, EpafiFilter, ErgasiaFilter, AithmaFilter, PolisiFilter, ServiceFilter, TrainingFilter, HardwareFilter
from .models import Dhmos, Employee, Ergasies, Adeia, Aithmata, Polisi, Service, Hardware, Training
from django.contrib.auth.decorators import login_required
from .add_records import dhmospost_new, epafi_new, ergasia_new, adeia_new, aithma_new, polisi_new, service_new, training_new, hardware_new
from .delete_records import delete_pelatis, delete_epafi, delete_ergasia, delete_adeia, delete_aithma, delete_polisi, \
    delete_service, delete_training, delete_hardware
from .export import export_pelates, export_contacts, export_ergasies, export_aithmata, export_adeia, export_training, export_hardware
from .update_records import pelatis_update, epafi_update, ergasia_update, adeia_update, aithma_update, polisi_update, \
    service_update, training_update, hardware_update
from .user_register import user_register
import datetime


@login_required(login_url="/accounts/login")
def home(request):
    return render(request, 'main/home.html')


@login_required
def pelatis(request):
    alldhmos = Dhmos.objects.all().order_by('name')
    pelatis_filter = PelatisFilter(request.GET, queryset=alldhmos)
    return render(request, 'main/pelatis.html', {'filter': pelatis_filter})


@login_required
def epafi(request):
    allepafes = Employee.objects.all().order_by('lastname')
    epafi_filter = EpafiFilter(request.GET, queryset=allepafes)
    return render(request, 'main/epafi.html', {'filter': epafi_filter})


@login_required
def ergasia(request):
    order_by = request.GET.get('order_by', '-importdate')
    today = datetime.date.today()
    allergasies = Ergasies.objects.filter(importdate__year=today.year).order_by(order_by)
    ergasies_filter = ErgasiaFilter(request.GET, queryset=allergasies)
    return render(request, 'main/ergasia.html', {'filter': ergasies_filter})


@login_required
def adeia(request):
    today = datetime.date.today()
    alladeies = Adeia.objects.filter(createddate__year=today.year,employee=request.user).order_by('-startdate')
    context = {'alladeies': alladeies}
    return render(request, 'main/adeia.html', context)


@login_required
def training(request):
    today = datetime.date.today()
    alltrainings = Training.objects.filter(importdate__year=today.year).order_by('-importdate')
    training_filter = TrainingFilter(request.GET, queryset=alltrainings)
    return render(request,'main/training.html', {'filter': training_filter})


@login_required
def aithma(request):
    today = datetime.date.today()
    allaithmata = Aithmata.objects.filter(importdate__year=today.year).order_by('-importdate')
    aithma_filter = AithmaFilter(request.GET, queryset=allaithmata)
    return render(request, 'main/aithma.html', {'filter': aithma_filter})


@login_required
def polisi(request):
    today = datetime.date.today()
    allpolisi = Polisi.objects.filter(katagrafi__year=today.year).order_by('-katagrafi')
    polisi_filter = PolisiFilter(request.GET, queryset=allpolisi)
    return render(request, 'main/polisi.html', {'filter': polisi_filter})


@login_required
def service(request):
    today = datetime.date.today()
    allservice = Service.objects.filter(importdate__year=today.year)
    service_filter = ServiceFilter(request.GET, queryset=allservice)
    return render(request, 'main/service.html', {'filter': service_filter})


@login_required
def hardware(request):
    allhardware = Hardware.objects.all()
    hardware_filter = HardwareFilter(request.GET, queryset=allhardware)
    return render(request, 'main/hardware.html', {'filter': hardware_filter})

@login_required
def ergasia_search(request):
    return render(request, 'search/ergasia_search.html')


@login_required
def adeia_search(request):
    return render(request, 'search/adeia_search.html')


@login_required
def polisi_search(request):
    return render(request,'search/polisi_search.html')