from django.shortcuts import redirect, get_object_or_404
from .models import *

def delete_prosfora(request, pk):
    object = Prosfora.objects.get(pk=pk)
    object.delete()
    return redirect('prosfora')

def delete_contract(request, pk):
    object = Contract.objects.get(pk=pk)
    object.delete()
    return redirect('symbasi')