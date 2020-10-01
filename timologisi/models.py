from django.db import models
from dhmoi.model_choices import *
import datetime

symbasi_type = (
    ('REL00','REL00'),
    ('HARD00','HARD00')
)

# Create your models here.
class Prosfora(models.Model):
    pelatis = models.ForeignKey('dhmoi.Dhmos', on_delete=models.CASCADE, verbose_name='Πελάτης', null=False,blank=False)
    send_date = models.DateField(default=datetime.date.today, verbose_name='Ημ.Κατάθ.', null=False, blank=False)
    app = models.CharField(max_length=150, choices=app_choice, verbose_name='Εφαρμογή', null=True, blank=True)
    contact_name = models.ForeignKey('dhmoi.Employee', on_delete=models.CASCADE, verbose_name='Επαφή', null=True, blank=True)
    poso = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Ποσό', null=False, blank=False)
    prosfora_info = models.TextField(max_length=700, verbose_name='Περ.Προσφ.', null=True, blank=True)
    is_approved = models.BooleanField(verbose_name='Συμβασιοποιήθηκε', default=False)

    @property
    def euro_amount(self):
        return "€%s" % self.poso if self.poso else ""
    
    class Meta:
        verbose_name = 'Προσφορά'
        verbose_name_plural = 'Προσφορά'
        ordering = ['id']
        #db_table = ""


class Symbasi(models.Model):
    pelatis = models.ForeignKey('dhmoi.Dhmos', on_delete=models.CASCADE, verbose_name='Πελάτης', null=False,blank=False)
    end_date = models.DateField(default=datetime.date.today, verbose_name='Ημ.Λήξης', null=False, blank=False)
    sign_date = models.DateField(default=datetime.date.today, verbose_name='Ημ.Υπογρ.', null=False, blank=False)
    symbasi = models.CharField(max_length=100, choices=symbasi_type, null=False, blank=False)
    epafi = models.ForeignKey('dhmoi.Employee', on_delete=models.CASCADE, verbose_name='Υπ.Επικ.', null=False, blank=False,default='empty')
    poso = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Ποσό', null=False, blank=False, default=0)
    #symbasi_code = models.PositiveIntegerField(default=0, null=False)
    symbasi_description = models.TextField(max_length=600, null=True, blank=True)

    @property
    def euro_amount(self):
        return "€%s" % self.poso if self.poso else ""

    class Meta:
        verbose_name = 'Σύμβαση'
        verbose_name_plural = 'Σύμβαση'
        ordering = ['id']

    
    

