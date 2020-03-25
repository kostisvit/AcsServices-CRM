from django import forms
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import DhmosForm, EmployeeForm, AdeiaForm, ErgasiaForm, AithmataForm, PolisiForm, ServiceForm
from .models import Dhmos, Employee, Ergasies, Adeia, Aithmata, Polisi, Service
from django.contrib.auth.models import User


@login_required
def dhmospost_new(request):
    if request.method == "POST":
        form = DhmosForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('pelatis')
    else:
        dhmosform = DhmosForm()
    return render(request, 'add_records/pelatis_new.html', {'dhmosform': dhmosform})


@login_required
def epafi_new(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('epafi')
    else:
        employeeform = EmployeeForm()
    return render(request, 'add_records/epafi_new.html', {'employeeform': employeeform})


@login_required
def ergasia_new(request):
    if request.method == "POST":
        form = ErgasiaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('ergasia')
    else:
        ergasiaform = ErgasiaForm(initial={'employee': request.user})
    return render(request, 'add_records/ergasia_new.html', {'ergasiaform': ergasiaform})


@login_required
def adeia_new(request):
    if request.method == "POST":
        form = AdeiaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('adeia')
    else:
        form = AdeiaForm(initial={'employee': request.user})  # initial={'employee':request.user}
    return render(request, 'add_records/adeia_new.html', {'adeiaform': form})


@login_required
def aithma_new(request):
    if request.method == "POST":
        form = AithmataForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('aithma')
    else:
        aithmataform = AithmataForm(initial={'assign': request.user})
    return render(request, 'add_records/aithmata_new.html', {'aithmataform': aithmataform})


@login_required
def polisi_new(request):
    if request.method == "POST":
        form = PolisiForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('polisi')
    else:
        form = PolisiForm()
    return render(request, 'add_records/polisi_new.html', {'polisiform': form})


@login_required
def service_new(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('service')
    else:
        form = ServiceForm()
    return render(request, 'add_records/service_new.html', {'serviceform': form})






