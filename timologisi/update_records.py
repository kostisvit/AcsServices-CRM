from timologisi.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import ProsforaForm, ContractForm

def prosfora_update(request, pk):
    post = get_object_or_404(Prosfora, pk=pk)
    if request.method == "POST":
        form = ProsforaForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('prosfora')
    else:
        form = ProsforaForm(instance=post)
    return render(request, 'update/prosfora-change.html', {'prosforaform': form})    



def symbasi_update(request, pk):
    post = get_object_or_404(Contract, pk=pk)
    if request.method == "POST":
        form = ContractForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('symbasi')
    else:
        form = ContractForm(instance=post)
    return render(request, 'update/symbasi-change.html', {'contractform': form})
