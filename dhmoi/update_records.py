from .models import Dhmos, Employee, Ergasies, Adeia, Aithmata, Polisi, Service
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import DhmosForm, EmployeeForm, ErgasiaForm, AdeiaForm, AithmataForm, PolisiForm, ServiceForm


@login_required
def pelatis_update(request, pk):
    post = get_object_or_404(Dhmos, pk=pk)
    if request.method == "POST":
        form = DhmosForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            post.save()
            return redirect('pelatis')
    else:
        form = DhmosForm(instance=post)
    return render(request, 'update_records/pelatis_update.html', {'dhmosform': form})


@login_required
def epafi_update(request, pk):
    post = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('epafi')
    else:
        form = EmployeeForm(instance=post)
    return render(request, 'update_records/epafi_update.html', {'employeeform': form})


@login_required
def ergasia_update(request, pk):
    post = get_object_or_404(Ergasies, pk=pk)
    if request.method == "POST":
        form = ErgasiaForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            post.save()
            return redirect('ergasia')
    else:
        form = ErgasiaForm(instance=post)
    return render(request, 'update_records/ergasia_update.html', {'ergasiaform': form})


@login_required
def adeia_update(request, pk):
    post = get_object_or_404(Adeia, pk=pk)
    if request.method == "POST":
        form = AdeiaForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('adeia')
    else:
        form = AdeiaForm(instance=post)
    return render(request, 'update_records/adeia_update.html', {'adeiaform': form})


@login_required
def aithma_update(request, pk):
    post = get_object_or_404(Aithmata, pk=pk)
    if request.method == "POST":
        form = AithmataForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('aithma')
    else:
        form = AithmataForm(instance=post)
    return render(request, 'update_records/aithma_update.html', {'aithmataform': form})


@login_required
def polisi_update(request, pk):
    post = get_object_or_404(Polisi, pk=pk)
    if request.method == "POST":
        form = PolisiForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('polisi')
    else:
        form = PolisiForm(instance=post)
    return render(request, 'update_records/polisi_update.html', {'polisiform': form})


@login_required
def service_update(request, pk):
    post = get_object_or_404(Service, pk=pk)
    if request.method == "POST":
        form = ServiceForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('service')
    else:
        form = ServiceForm(instance=post)
    return render(request, 'update_records/service_update.html', {'serviceform': form})
