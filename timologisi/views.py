from django.shortcuts import render,redirect
from .forms import ProsforaForm, ContractForm, InvoiceForm
from .models import *
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
import json
from dhmoi.models import *
from django.core import serializers
from django.http import JsonResponse
import datetime
from .filters import *

def prosfora(request):
    
    today = datetime.date.today()
    
    form = ProsforaForm()
    if request.method == 'POST':
        form = ProsforaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('prosfora')
    
    allprosfores = Prosfora.objects.filter(date_send__year=today.year)
    prosfora_filter = ProsforaFilter(request.GET, queryset=allprosfores)
    context = {'prosforaform': form , 'allprosfores': allprosfores, 'filter': prosfora_filter}
    return render(request,'main/prosfora.html', context)


def symbasi(request,pk=-1):
    today = datetime.date.today()
    if pk!= -1:
        post = get_object_or_404(Prosfora, pk=pk)
        post.is_approved = True
        post.save()
    form = ContractForm()
    #form2 = InvoiceForm()
    if request.method == 'POST':
        form = ContractForm(request.POST)
       # form2 = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContractForm()
        #if form1.is_valid():
         #   form2.save()
    else:
        if pk!= -1:
            form = ContractForm(instance=post)
        else:
            form = ContractForm()
    #allcontract = Contract.objects.all()
    allcontract = Contract.objects.filter(contract_sign__year=today.year)
    contract_filter=ContractFilter(request.GET, queryset=allcontract)
    context = {'contractform': form, 'allcontract': allcontract, 'filter': contract_filter}
    return render(request,'main/symbasi.html', context)


def timologio(request):
    form = InvoiceForm()
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'invoiceform': form }
    return render(request,'main/timologisi.html', context)





###chained dropdownlist views

def api_dhmos_prosfora(request,pk):
    allepafes = Employee.objects.all().filter(dhmos_id=pk).order_by('lastname')
    epafesSerialized = serializers.serialize ('json', allepafes, ensure_ascii=False)
    return JsonResponse(json.loads(epafesSerialized), safe=False)