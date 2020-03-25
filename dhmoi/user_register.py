from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages


# Φόρμα εγγραφής χρήστη στην εφαρμογή
def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'register.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Το Username υπάρχει,επιλέξτε άλλο.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Το Email υπάρχει,επιλέξτε άλλο'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Το Password δεν ταιριάζει.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.is_active = False
                user.save()
                messages.success(request, 'Ο χρήστης δημιουργήθηκε επιτυχώς.')

                # redirect to accounts page:
                # return redirect('/accounts/login')


    else:
        form = RegisterForm()

    return render(request, template, {'form': form})
