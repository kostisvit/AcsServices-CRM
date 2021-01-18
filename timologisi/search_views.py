from django.shortcuts import render,redirect
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import *
from .filters import *
import datetime

def prosforasearch(request):
    #order_by = request.GET.get('order_by', '-importdate')
    today = datetime.date.today()
    allprosfores = Prosfora.objects.filter(date_send__year=today.year)
    prosfora_filter = ProsforaFilter(request.GET, queryset=allprosfores)
    return render(request, 'search/prosfora_search.html', {'filter': prosfora_filter})