from django import forms
from django.forms import ModelForm
from .models import Prosfora, Contract, Invoice
from dhmoi.models import Dhmos, Employee
from django.forms import ModelChoiceField
from dhmoi.model_choices import *


from bootstrap_datepicker_plus import DatePickerInput


class NameChoiceField(ModelChoiceField):

    def label_from_instance(self, obj):
        return '{lastname} {firstname}'.format(lastname=obj.lastname, firstname=obj.firstname)
class DateInput(forms.DateInput):
    input_type = 'date'



class ProsforaForm(ModelForm):
    pelatis = ModelChoiceField(queryset=Dhmos.objects.order_by('name'), label='Πελάτης', required=True)
    app = forms.CharField( label='Εφαρμογή',required=False)
    contact = NameChoiceField(queryset=Employee.objects.order_by('lastname'), label='Υπάλληλος Επικοιν.', required=False)
    poso = forms.DecimalField(required=False,label='Ποσό')
    prosfora_des = forms.CharField(required=False, label='Περιγραφή',widget=forms.Textarea(attrs={'style': 'width:800px;'}))
    
    class Meta:
        model = Prosfora
        fields = ['pelatis', 'app','contact','poso','date_send','prosfora_des']
        widgets = {
            'date_send': DatePickerInput(format='%d/%m/%Y'), 
        }
        

class ContractForm(ModelForm):
    pelatis = ModelChoiceField(queryset=Dhmos.objects.order_by('name'), label='Πελάτης', required=True)
    contact = NameChoiceField(queryset=Employee.objects.order_by('lastname'), label='Υπάλληλος Επικοιν.', required=False)
    contract_desc = forms.CharField(required=False, label='Περιγραφή',widget=forms.Textarea(attrs={'style': 'width:500px; height: 80px;'}))
    class Meta:
        model = Contract
        fields = '__all__'
        widgets = {
            'contract_sign': DatePickerInput(format='%d/%m/%Y'),
            'contract_end': DatePickerInput(format='%d/%m/%Y'),
        }

class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'