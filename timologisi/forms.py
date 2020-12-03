from django.forms import ModelForm
from .models import Prosfora, Contract, Invoice

class ProsforaForm(ModelForm):
    class Meta:
        model = Prosfora
        fields = '__all__'

class ContractForm(ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'

class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'