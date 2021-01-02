from __future__ import unicode_literals
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


class ProsforaAdmin(ImportExportModelAdmin):
   list_display = ('pelatis', 'app', 'contact', 'poso','is_approved','prosfora_des','created_at','updated_at')

class ContractAdmin(ImportExportModelAdmin):
    list_display = ('pelatis','contract_end','contract_sign','contract_code','contact','poso','contract_desc','combined')
    
class InvoiceAdmin(ImportExportModelAdmin):
    list_display = ('pelatis','contract_code','invoice_date','poso','bank','is_paid')



admin.site.register(Prosfora,ProsforaAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Invoice, InvoiceAdmin)