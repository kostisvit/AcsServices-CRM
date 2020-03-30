from django import forms
from .models import Dhmos, Employee, Ergasies, Adeia, Aithmata, Polisi, Service, Training, Hardware
from django.forms import ModelChoiceField
from django.contrib.auth.models import User


class DateInput(forms.DateInput):
    input_type = 'date'


class NameChoiceField(ModelChoiceField):

    def label_from_instance(self, obj):
        return '{lastname} {firstname}'.format(lastname=obj.lastname, firstname=obj.firstname)


class UserModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return '{last_name} {first_name}'.format(last_name=obj.last_name, first_name=obj.first_name)


class DhmosForm(forms.ModelForm):
    is_visible = forms.BooleanField(required=False, label="Ενεργός")

    class Meta:
        model = Dhmos
        fields = '__all__'


class EmployeeForm(forms.ModelForm):
    dhmos = ModelChoiceField(queryset=Dhmos.objects.order_by('name'), label='Πελάτης', required=True)
    is_visible = forms.BooleanField(required=False, label="Ενεργός")

    class Meta:
        model = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['dhmos'].queryset = Dhmos.objects.order_by('name').filter(is_visible=True)

   


class ErgasiaForm(forms.ModelForm):
    dhmos = ModelChoiceField(queryset=Dhmos.objects.order_by('name'), label='Πελάτης', required=True)
    name = NameChoiceField(queryset=Employee.objects.order_by('lastname'), label='Υπάλληλος Επικοιν.', required=True)
    employee = UserModelChoiceField(queryset=User.objects.order_by('last_name').filter(is_active=True),label='Υπάλληλος ACS')

    class Meta:
        model = Ergasies
        fields = '__all__'
        fields = ['importdate', 'app', 'dhmos', 'name', 'jobtype',
                  'info', 'text', 'employee', 'time', 'ticketid']
        widgets = {
            'importdate': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(ErgasiaForm, self).__init__(*args, **kwargs)
        super(ErgasiaForm, self).__init__(*args, **kwargs)
        self.fields['dhmos'].queryset = Dhmos.objects.order_by('name').filter(is_visible=True)
        self.fields['name'].queryset = Employee.objects.order_by('lastname').filter(is_visible=True)
        


class AdeiaForm(forms.ModelForm):
    employee = UserModelChoiceField(queryset=User.objects.order_by('last_name').filter(is_active=True),label='Υπάλληλος ACS')

    class Meta:
        model = Adeia
        fields = '__all__'
        widgets = {
            'startdate': DateInput(),
            'enddate': DateInput(),
            'createddate': DateInput(),
        }


class AithmataForm(forms.ModelForm):
    dhmos = ModelChoiceField(queryset=Dhmos.objects.order_by('name'), label='Πελάτης', required=True)
    employee = NameChoiceField(queryset=Employee.objects.order_by('lastname'), label='Υπάλληλος Επικοιν.',required=False)
    assign = UserModelChoiceField(queryset=User.objects.order_by('last_name').filter(is_active=True), label='Χρέωση')

    class Meta:
        model = Aithmata
        fields = '__all__'
        widgets = {
            'importdate': DateInput(),
            'closedate': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(AithmataForm, self).__init__(*args, **kwargs)
        super(AithmataForm, self).__init__(*args, **kwargs)
        self.fields['dhmos'].queryset = Dhmos.objects.order_by('name').filter(is_visible=True)
        self.fields['employee'].queryset = Employee.objects.order_by('lastname').filter(is_visible=True)


class PolisiForm(forms.ModelForm):
    dhmos = ModelChoiceField(queryset=Dhmos.objects.order_by(
        'name'), label='Πελάτης', required=True)

    class Meta:
        model = Polisi
        fields = '__all__'
        widgets = {
            'katagrafi': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(PolisiForm, self).__init__(*args, **kwargs)
        self.fields['dhmos'].queryset = Dhmos.objects.filter(is_visible=True)


class ServiceForm(forms.ModelForm):
    employee = UserModelChoiceField(queryset=User.objects.order_by('last_name').filter(is_active=True),
                                    label='Υπάλληλος ACS')

    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'importdate': DateInput(),
            'exportdate': DateInput(),
        }



class TrainingForm(forms.ModelForm):
    employee = UserModelChoiceField(queryset=User.objects.order_by('last_name').filter(is_active=True),label='Υπάλληλος ACS')

    class Meta:
        model = Training
        fields = '__all__'
        widgets = {
            'importdate': DateInput(),
        }


class HardwareForm(forms.ModelForm):
    employee = UserModelChoiceField(queryset=User.objects.order_by('last_name').filter(is_active=True),label='Υπάλληλος ACS')
    class Meta:
        model = Hardware
        fields = '__all__'



class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_repeat = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
