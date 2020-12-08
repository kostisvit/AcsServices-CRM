from django.shortcuts import render,redirect
from .forms import ProsforaForm, ContractForm, InvoiceForm
from .models import *
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404

def prosfora(request):
    form = ProsforaForm()
    if request.method == 'POST':
        form = ProsforaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prosfora')
    allprosfores = Prosfora.objects.all()
    context = {'prosforaform': form , 'allprosfores': allprosfores}
    return render(request,'main/prosfora.html', context)


def symbasi(request,pk=-1):
    if pk!= -1:
        post = get_object_or_404(Prosfora, pk=pk)
        post.is_approved = True
        post.save()
        
    form1 = ContractForm()
    form2 = InvoiceForm()
    
    if request.method == 'POST':
        form1 = ContractForm(request.POST,instance=post)
        form2 = InvoiceForm(request.POST)
        if form1.is_valid():
            form2.save()
        if form1.is_valid():
            form2.save()
    else:
        if pk!= -1:
            form1 = ContractForm(instance=post)
        else:
            form1 = ContractForm()
            
    context = {'contractform': form1, 'invoiceform': form2}
    return render(request,'main/symbasi.html', context)


def timologio(request):
    form = InvoiceForm()
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'invoiceform': form }
    return render(request,'main/timologisi.html', context)


def prosfora_all(request):
    allprosfores = Prosfora.objects.all()
    context = {'allprosfores': allprosfores}
    return render(request,'main/prosfora.html', context)