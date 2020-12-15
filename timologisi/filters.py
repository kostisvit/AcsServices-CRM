from .models import *
import django_filters
from django.contrib.auth.models import User
from django_filters.widgets import RangeWidget
from django.forms import ModelChoiceField
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'



class ProsforaFilter(django_filters.FilterSet):
    class Meta:
        model = Prosfora
        fields = ['pelatis','is_approved']