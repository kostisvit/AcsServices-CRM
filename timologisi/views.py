from django.shortcuts import render
from .forms import ProsforaForm, ContractForm, InvoiceForm


def prosfora(request):
    form = ProsforaForm()
    if request.method == 'POST':
        form = ProsforaForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'prosforaform': form }
    return render(request,'main/prosfora.html', context)


def symbasi(request):
    form1 = ContractForm()
    form2 = InvoiceForm()
    if request.method == 'POST':
        form1 = ContractForm(request.POST)
        form2 = InvoiceForm(request.POST)
        if form1.is_valid():
            form2.save()
        if form1.is_valid():
            form2.save()
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
