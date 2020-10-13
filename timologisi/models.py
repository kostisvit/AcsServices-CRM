from django.db import models
from dhmoi.model_choices import *
import datetime

class Prosfora(models.Model):
    pelatis = models.ForeignKey('dhmoi.Dhmos', on_delete=models.CASCADE, null=False, blank=False)
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

