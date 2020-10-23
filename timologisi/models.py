from django.db import models
from dhmoi.model_choices import *
import datetime


contract_choice = (
    ('HARD00','HARD00'),
    ('SOFT00','SOFT00')
)

class Prosfora(models.Model):
    pelatis = models.ForeignKey('dhmoi.Dhmos', db_index=True, on_delete=models.CASCADE, null=False, blank=False)
    app = models.CharField(max_length=100, choices=app_choice, null=True, blank=True)
    contact = models.ForeignKey('dhmoi.Employee', on_delete=models.CASCADE, null=False, blank=False)
    poso = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    is_approved = models.BooleanField(default=False)
    prosfora_des = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = 'Προσφορά'
        verbose_name_plural = 'Προσφορά'
        ordering = ['id']

    #def combined(obj): 
     #   return "%s %s" % (obj.app, obj.id)

class Contract(models.Model):
    pelatis = models.ForeignKey('dhmoi.Dhmos', db_index=True, on_delete=models.CASCADE, null=False, blank=False)
    contract_end = models.DateField(verbose_name=' Ημ.Λήξης', null=False, blank=False)
    contract_sign = models.DateField(verbose_name=' Ημ.Υπογραφ.', null=False, blank=False)
    contract_code = models.CharField(max_length=150, choices=contract_choice, verbose_name='Κωδικός Σύμβ.', null=False, blank=False)
    contact = models.ForeignKey('dhmoi.Employee', on_delete=models.CASCADE, verbose_name='Επαφή', null=True, blank=True)
    contract_ammount = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Ποσό Σύμβασης')
    contract_desc = models.TextField(verbose_name='Περιγραφή Σύμβασης', null=True, blank=True)

    class Meta:
        verbose_name = 'Σύμβαση'
        verbose_name_plural = 'Σύμβαση'
        ordering = ['id']

    def combined(obj):
        return "%s %s" % (obj.contract_code, obj.id)