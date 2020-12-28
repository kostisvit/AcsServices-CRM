from .models import *
import django_filters
from django.contrib.auth.models import User
from django_filters.widgets import RangeWidget
from django.forms import ModelChoiceField
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'




class ProsforaFilter(django_filters.FilterSet):
    choices = (
    (True, "YES"),
    (False, "NO")
    )
    
    is_approved = django_filters.ChoiceFilter(choices=choices, label='Αποδοχή')
    class Meta:
        model = Prosfora
        fields = ['pelatis','is_approved']
        


class ContractFilter(django_filters.FilterSet):

    class Meta:
        model = Contract
        fields = ['pelatis']


class InvoiceFilter(django_filters.FilterSet):
    bank_choice = (
    ('Τράπεζα Πειραιώς','Τράπεζα Πειραιώς'),
    ('Εθνική Τράπεζα','Εθνική Τράπεζα'),
    ('AlphaBank','AlphaBank'),
    ('EuroBank','Eurobank')
    )

    bank = django_filters.ChoiceFilter(choices=bank_choice, label='Τράπεζα')

    class Meta:
        model = Invoice
        fields = ['pelatis','bank']