from .models import Dhmos, Employee, Ergasies, Adeia, Aithmata, Polisi, Service, Training, Hardware
import django_filters
from django_filters import DateRangeFilter,DateFilter
from django.contrib.auth.models import User
from django_filters.widgets import RangeWidget
from django.forms import ModelChoiceField
from django import forms



class DateInput(forms.DateInput):
    input_type = 'date'


class NameChoiceField(ModelChoiceField):

    def label_from_instance(self, obj):
        return '{lastname} {firstname}'.format(lastname=obj.lastname, firstname=obj.firstname)


class UserModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return '{last_name} {first_name}'.format(last_name=obj.last_name, first_name=obj.first_name)




class PelatisFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Πελάτης')

    class Meta:
        model = Dhmos
        fields = ['name', 'phone']


class EpafiFilter(django_filters.FilterSet):
    dhmos = django_filters.ModelChoiceFilter(queryset=Dhmos.objects.all(),label='Φορέας')
    lastname = django_filters.CharFilter(lookup_expr='icontains', label='Επώνυμο')

    class Meta:
        model = Employee
        fields = ['dhmos', 'firstname', 'lastname']

    def __init__(self, *args, **kwargs):
        super(EpafiFilter, self).__init__(*args, **kwargs)
        if self.data == {}:
            self.queryset = self.queryset.none()


job_choice = (
    ('TeamViewer', 'TeamViewer'),
    ('Επίσκεψη', 'Επίσκεψη'),
    ('Γραφείο', 'Γραφείο')
)


class ErgasiaFilter(django_filters.FilterSet):
    dhmos = django_filters.ModelChoiceFilter(queryset=Dhmos.objects.filter(is_visible=True),label='Φορέας')
    jobtype = django_filters.ChoiceFilter(choices=job_choice, label='Τύπος')
    employee = django_filters.ModelChoiceFilter(queryset=User.objects.filter(is_active=True))
    class Meta:
        model = Ergasies
        fields = ['dhmos', 'app', 'employee', 'jobtype']

    def __init__(self, *args, **kwargs):
        super(ErgasiaFilter, self).__init__(*args, **kwargs)
        if self.data == {}:
            self.queryset = self.queryset.none()


class ErgasiaFilterAll(django_filters.FilterSet):
    dhmos = django_filters.ModelChoiceFilter(queryset=Dhmos.objects.filter(is_visible=True),label='Φορέας')
    jobtype = django_filters.ChoiceFilter(choices=job_choice, label='Τύπος')
    employee = django_filters.ModelChoiceFilter(queryset=User.objects.filter(is_active=True))
    importdate = django_filters.NumberFilter(lookup_expr='year', label='Έτος')
    class Meta:
        model = Ergasies
        fields = ['dhmos', 'app', 'employee', 'jobtype']
    
    def __init__(self, *args, **kwargs):
        super(ErgasiaFilterAll, self).__init__(*args, **kwargs)
        if self.data == {}:
            self.queryset = self.queryset.none()

 


class AithmaFilter(django_filters.FilterSet):
    dhmos = django_filters.ModelChoiceFilter(queryset=Dhmos.objects.filter(is_visible=True),label='Φορέας')
    employee = django_filters.CharFilter(lookup_expr='icontains', label='Υπάλληλος')
    assign = django_filters.ModelChoiceFilter(queryset=User.objects.filter(is_active=True))
    class Meta:
        model = Aithmata
        fields = ['dhmos', 'employee', 'assign']

    

polisi_choice = (
    ('OPEN', 'OPEN'),
    ('CLOSED', 'CLOSED')
)


class PolisiFilter(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(choices=polisi_choice, label='Κατάσταση')

    class Meta:
        model = Polisi
        fields = ['dhmos', 'etos', 'status']

    def __init__(self, *args, **kwargs):
        super(PolisiFilter, self).__init__(*args, **kwargs)
        if self.data == {}:
            self.queryset = self.queryset.none()


class PolisiFilterAll(django_filters.FilterSet):
    dhmos = django_filters.ModelChoiceFilter(queryset=Dhmos.objects.filter(is_visible=True),label='Φορέας')
    status = django_filters.ChoiceFilter(choices=polisi_choice, label='Κατάσταση')

    class Meta:
        model = Polisi
        fields = ['dhmos', 'etos', 'status']

    def __init__(self, *args, **kwargs):
        super(PolisiFilterAll, self).__init__(*args, **kwargs)
        if self.data == {}:
            self.queryset = self.queryset.none()


class ServiceFilter(django_filters.FilterSet):
    customername = django_filters.CharFilter(
        lookup_expr='icontains', label='Όνομα πελάτη')

    class Meta:
        model = Service
        fields = ['customername', 'phone', 'cellphone', 'employee', 'year']


foreas_choice = (
    ('OTS', 'OTS'),
    ('Interlei', 'Interlei'),
    ('ACS','ACS')
)


class TrainingFilter(django_filters.FilterSet):
    foreas = django_filters.ChoiceFilter(choices=foreas_choice, label='Φορέας')
    employee = django_filters.ModelChoiceFilter(queryset=User.objects.filter(is_active=True))
    class Meta:
        model = Training
        fields = ['foreas', 'employee']
        

    def __init__(self, *args, **kwargs):
        super(TrainingFilter, self).__init__(*args, **kwargs)
        if self.data == {}:
            self.queryset = self.queryset.none()


class HardwareFilter(django_filters.FilterSet):
    employee = django_filters.ModelChoiceFilter(queryset=User.objects.filter(is_active=True))
    class Meta:
        model = Hardware
        fields = ['employee', ]

    def __init__(self, *args, **kwargs):
        super(HardwareFilter, self).__init__(*args, **kwargs)
        if self.data == {}:
            self.queryset = self.queryset.none()
