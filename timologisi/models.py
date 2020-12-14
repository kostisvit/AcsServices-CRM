from django.db import models
from dhmoi.model_choices import *
import datetime


def current_year():
    return datetime.date.today().year


contract_choice = (
    ('HARD00','HARD00'),
    ('SOFT00','SOFT00')
)

bank_choice = (
    ('Τράπεζα Πειραιώς','Τράπεζα Πειραιώς'),
    ('Εθνική Τράπεζα','Εθνική Τράπεζα'),
    ('AlphaBank','AlphaBank'),
    ('EuroBank','Eurobank')
)

class Prosfora(models.Model):
    pelatis = models.ForeignKey('dhmoi.Dhmos', db_index=True, on_delete=models.CASCADE, null=False, blank=False)
    app = models.CharField(max_length=150, null=True, blank=True)
    contact = models.ForeignKey('dhmoi.Employee', on_delete=models.CASCADE, null=False, blank=False)
    poso = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    date_send = models.DateField(verbose_name=' Ημ.Αποστολής', null=False, blank=False)
    is_approved = models.BooleanField(default=False)
    prosfora_des = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = 'Προσφορά'
        verbose_name_plural = 'Προσφορά'
        ordering = ['id']
    
    #@property
    #def price_display(self):
    #    return "€%s" % self.poso

    #def combined(obj): 
     #   return "%s %s" % (obj.app, obj.id)

class Contract(models.Model):
    pelatis = models.ForeignKey('dhmoi.Dhmos', db_index=True, on_delete=models.CASCADE, null=False, blank=False)
    contract_end = models.DateField(verbose_name=' Ημ.Λήξης', null=False, blank=False)
    contract_sign = models.DateField(verbose_name=' Ημ.Υπογραφ.', null=False, blank=False)
    contract_code = models.CharField(max_length=150, choices=contract_choice, verbose_name='Κωδικός Σύμβ.', null=False, blank=False)
    contact = models.ForeignKey('dhmoi.Employee', on_delete=models.CASCADE, verbose_name='Επαφή', null=True, blank=True)
    poso = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Ποσό Σύμβασης')
    contract_desc = models.TextField(verbose_name='Περιγραφή Σύμβασης', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Σύμβαση'
        verbose_name_plural = 'Σύμβαση'
        ordering = ['id']

    def combined(obj):
        return "%s %s" % (obj.contract_code, obj.id)

    def __str__(self):
        return (self.contract_code) + ' ' + str(self.id)
    
    

class Invoice(models.Model):
    payment_choice = (
        ('Δόσεις','Δόσεις'),
        ('Εφάπαξ','Εφάπαξ')
    )
    pelatis = models.ForeignKey('dhmoi.Dhmos', db_index=True, on_delete=models.CASCADE, null=False, blank=False)
    contract_code = models.ForeignKey('Contract', on_delete=models.CASCADE, null=False, blank=False, verbose_name='Κωδ.Συμβ.')
    invoice_date = models.DateField(verbose_name=' Ημ.Τιμολόγησης', null=False, blank=False)
    invoice_code = models.IntegerField(verbose_name='Κωδ.Τιμ', null=False, blank=True, default=0)
    amount = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Ποσό')
    bank = models.CharField(max_length=150, choices=bank_choice, verbose_name='Τράπεζα', null=False, blank=False)
    payment_type = models.CharField(max_length=150,choices=payment_choice,verbose_name='Τύπος πληρωμής', default='------', null=False,blank=False)
    payment_date = models.DateField(default=datetime.date.today)
    is_paid = models.BooleanField(default=False, verbose_name='Πληρώθηκε')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Τιμολόγηση'
        verbose_name_plural = 'Τιμολόγηση'
        ordering = ['id']
    
    