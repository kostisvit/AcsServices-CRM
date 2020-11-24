from django.shortcuts import render
from django.contrib.auth.models import User
from .filters import *
from .models import Dhmos, Employee, Ergasies, Adeia, Aithmata, Polisi, Service, Hardware, Training
from django.contrib.auth.decorators import login_required
from .add_records import *
from .delete_records import *
from .export import *
from .update_records import *
from .user_register import user_register
from .charts import *
import datetime
#from django.views.decorators.cache import cache_page

from tasks.views import index
from tasks.models import *
from tasks import context_processor

from timologisi.views import *

from django.core import serializers
from django.http import JsonResponse

import json

from django.contrib.auth import logout


from django.views.generic import TemplateView, ListView
from django.db.models import Q

from django.db.models import Sum

def logout(request):
     response.delete_cookie('user_location')
     return response

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
    alladeies = Adeia.objects.filter(createddate__year=today.year, employee=request.user).order_by('-startdate')
    context = {'alladeies': alladeies}
    return render(request, 'main/adeia.html', context)



@login_required
def training(request):
    today = datetime.date.today()
    alltrainings = Training.objects.filter(importdate__year=today.year).order_by('-importdate')
    training_filter = TrainingFilter(request.GET, queryset=alltrainings)
    return render(request, 'main/training.html', {'filter': training_filter})



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
def tameiaki(request):
    return render(request, 'main/tameiaki.html' )


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
    return render(request, 'search/polisi_search.html')

# chained selection view


@login_required
def api_dhmos(request,pk):
    allepafes = Employee.objects.all().filter(dhmos_id=pk).order_by('lastname')
    #epafi_filter = EpafiFilter(request.GET, queryset=allepafes)
    #return render(request, 'main/epafi.html', {'filter': epafi_filter})
    epafesSerialized = serializers.serialize ('json', allepafes, ensure_ascii=False)
    return JsonResponse(json.loads(epafesSerialized), safe=False)



@login_required
def api_dhmos_update(request,pk):
    allepafes = Employee.objects.all().filter(dhmos_id=pk).order_by('lastname')
    #epafi_filter = EpafiFilter(request.GET, queryset=allepafes)
    #return render(request, 'main/epafi.html', {'filter': epafi_filter})
    epafesSerialized = serializers.serialize ('json', allepafes, ensure_ascii=False)
    return JsonResponse(json.loads(epafesSerialized), safe=False)



@login_required
def api_aithma(request,pk):
    allepafes = Employee.objects.all().filter(dhmos_id=pk).order_by('lastname')
    #epafi_filter = EpafiFilter(request.GET, queryset=allepafes)
    #return render(request, 'main/epafi.html', {'filter': epafi_filter})
    epafesSerialized = serializers.serialize ('json', allepafes, ensure_ascii=False)
    return JsonResponse(json.loads(epafesSerialized), safe=False)



class SearchResultsView(ListView):
    model = Ergasies
    template_name = 'search/ergasia_search.html'

    def get_queryset(self): # new
        
        query = self.request.GET.get('q')
        if query:
            object_list = Ergasies.objects.filter(
             Q(info__icontains=query) | Q(dhmos__name__icontains=query) | Q(name__icontains=query)
        )
        else:
           object_list = None
        return object_list


class ChartView(TemplateView):
    template_name = 'charts/adeia_chart.html'

    def get_context_data(self, **kwargs):
        today = datetime.date.today()
        context = super().get_context_data(**kwargs)
        context["qs"] = Adeia.objects.values('employee__first_name','employee__last_name').filter(createddate__year=today.year).annotate(days=Sum('days'))
        return context
   

