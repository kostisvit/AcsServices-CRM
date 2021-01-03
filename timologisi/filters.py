from .models import *
import django_filters
from django.contrib.auth.models import User
from django_filters.widgets import RangeWidget
from django.forms import ModelChoiceField
from django import forms
from dhmoi.models import Dhmos

class DateInput(forms.DateInput):
    input_type = 'date'




class ProsforaFilter(django_filters.FilterSet):
    choices = (
    (True, "YES"),
    (False, "NO")
    )
    pelatis = django_filters.ModelChoiceFilter(queryset=Dhmos.objects.filter(is_visible=True),label='Φορέας')
    is_approved = django_filters.ChoiceFilter(choices=choices, label='Αποδοχή')
    date_send = django_filters.DateFromToRangeFilter(label='Αποστολή Προσφ. Από - Έως',widget=django_filters.widgets.RangeWidget(attrs={'placeholder': 'dd/mm/yyyy','type': 'date'}))
    date_send_exact = django_filters.DateFilter(label='Ημ. Αποστολής' ,widget=DateInput(attrs={'class': 'datepicker'}))
    class Meta:
        model = Prosfora
        fields = ['pelatis','is_approved','date_send','date_send_exact']
        


class ContractFilter(django_filters.FilterSet):
    pelatis = django_filters.ModelChoiceFilter(queryset=Dhmos.objects.filter(is_visible=True),label='Φορέας')
    contract_sign = django_filters.DateFilter(label='Ημ. Υπογραφής', widget=DateInput(attrs={'class': 'datepicker'}))
    contract_end = django_filters.DateFilter(label='Ημ. Λήξης', widget=DateInput(attrs={'class': 'datepicker'}))
    class Meta:
        model = Contract
        fields = ['pelatis','contract_sign','contract_end']


class InvoiceFilter(django_filters.FilterSet):
    bank_choice = (
    ('Τράπεζα Πειραιώς','Τράπεζα Πειραιώς'),
    ('Εθνική Τράπεζα','Εθνική Τράπεζα'),
    ('AlphaBank','AlphaBank'),
    ('EuroBank','Eurobank')
    )

    payment_choice = (
        ('Δόσεις','Δόσεις'),
        ('Εφάπαξ','Εφάπαξ')
    )

    is_paid_choices = (
    (True, "ΝΑΙ"),
    (False, "ΟΧΙ")
    )
    pelatis = django_filters.ModelChoiceFilter(queryset=Dhmos.objects.filter(is_visible=True), label='Φορέας')
    bank = django_filters.ChoiceFilter(choices=bank_choice, label='Τράπεζα')
    invoice_date = django_filters.DateFilter(label='Ημ. Τιμολόγησης', widget=DateInput(attrs={'class': 'datepicker'}))
    invoice_code = django_filters.CharFilter(label='Κωδ. Τιμολογίου')
    payment_type = django_filters.ChoiceFilter(choices=payment_choice, label='Τρόπος Πληρ.')
    payment_date = django_filters.DateFilter(label='Ημ. Πληρωμής',widget=DateInput(attrs={'class': 'datepicker'}))
    is_paid = django_filters.ChoiceFilter(choices=is_paid_choices)
    class Meta:
        model = Invoice
        fields = ['pelatis','bank','invoice_date','invoice_code','payment_type','payment_date','is_paid']