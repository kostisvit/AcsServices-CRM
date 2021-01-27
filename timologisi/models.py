from django.db import models
from dhmoi.model_choices import *
import datetime
import os
from django.utils.text import slugify

def current_year():
    return datetime.date.today().year


class Prosfora(models.Model):
    def user_directory_path(instance, filename):
        return 'pel_prosf__{0}/{1}'.format(instance.pelatis, filename)

    pelatis = models.ForeignKey('dhmoi.Dhmos', db_index=True, on_delete=models.CASCADE, null=False, blank=False)
    app = models.CharField(max_length=150, null=True, blank=True)
    contact = models.ForeignKey('dhmoi.Employee', on_delete=models.CASCADE, null=False, blank=False)
    poso = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    tax_poso = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False, default='0.00')
    date_send = models.DateField(verbose_name=' Ημ.Αποστολής', null=False, blank=False)
    document = models.FileField(upload_to=user_directory_path, default='-', blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    is_ongoing = models.BooleanField(default=False)
    prosfora_des = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Προσφορά'
        verbose_name_plural = 'Προσφορά'
        ordering = ['id']
    
    def tax_calculate(instance): #υπολογισμός ΦΠΑ
        result = float(instance.poso) * 1.24
        return result

    def save(self,*args, **kwargs):
        self.tax_poso = self.tax_calculate()
        super(Prosfora,self).save(*args,**kwargs)
    
    def sub_tax_poso(self): #Αφαίρεση ΦΠΑ απο το τελικό ποσό
        return self.tax_poso - self.poso

    def filename(self):
        return os.path.basename(self.document.name) #return only the file not the full path
    
    def delete(self, *args, **kwargs): #delete also the file
        self.document.delete()
        super().delete(*args, **kwargs)


class Contract(models.Model):
    def user_directory_path(instance, filename):
        return 'pel_contr__{0}/{1}'.format(instance.pelatis, filename)

    contract_choice = (
    ('HARD00','HARD00'),
    ('SOFT00','SOFT00'),
    ('SERV00','SERV00')
    )

    pelatis = models.ForeignKey('dhmoi.Dhmos', db_index=True, on_delete=models.CASCADE, null=False, blank=False)
    contract_end = models.DateField(verbose_name=' Ημ.Λήξης', null=False, blank=False)
    contract_sign = models.DateField(verbose_name=' Ημ.Υπογραφ.', null=False, blank=False)
    contract_code = models.CharField(max_length=150, choices=contract_choice, verbose_name='Κωδικός Σύμβ.', null=False, blank=False)
    contact = models.ForeignKey('dhmoi.Employee', on_delete=models.CASCADE, verbose_name='Επαφή', null=True, blank=True)
    poso = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Ποσό Σύμβασης')
    file = models.FileField(upload_to=user_directory_path, default='-', blank=True, null=True)
    contract_desc = models.TextField(verbose_name='Περιγραφή Σύμβασης', null=True, blank=True)
    slug = models.SlugField(unique=True, allow_unicode=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Σύμβαση'
        verbose_name_plural = 'Σύμβαση'
        ordering = ['id']
        
    
    def filename(self):
        return os.path.basename(self.file.name) 
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        value = self.contract_code
        self.slug = slugify(value, allow_unicode=False) + '' + str(self.id)
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs): #delete also the file
        self.file.delete()
        super().delete(*args, **kwargs)
    
    

class Invoice(models.Model):
    payment_choice = (
        ('Δόσεις','Δόσεις'),
        ('Εφάπαξ','Εφάπαξ')
    )

    bank_choice = (
    ('Τράπεζα Πειραιώς','Τράπεζα Πειραιώς'),
    ('Εθνική Τράπεζα','Εθνική Τράπεζα'),
    ('AlphaBank','AlphaBank'),
    ('EuroBank','Eurobank')
    )

    contract_choice = (
    ('HARD00','HARD00'),
    ('SOFT00','SOFT00')
    )

    pelatis = models.ForeignKey('dhmoi.Dhmos', db_index=True, on_delete=models.CASCADE, null=False, blank=False)
    slug = models.SlugField(blank=True)
    invoice_date = models.DateField(verbose_name=' Ημ.Τιμολόγησης', null=False, blank=False)
    invoice_code = models.IntegerField(verbose_name='Κωδ.Τιμ', null=False, blank=True, default=0)
    poso = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Ποσό')
    bank = models.CharField(max_length=150, choices=bank_choice, verbose_name='Τράπεζα', null=False, blank=False)
    payment_type = models.CharField(max_length=150,choices=payment_choice,verbose_name='Τύπος πληρωμής', default='------', null=False,blank=False)
    payment_date = models.DateField(default=datetime.date.today, verbose_name='Ημ.Πληρωμ.')
    is_paid = models.BooleanField(default=False, verbose_name='Πληρώθηκε')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    class Meta:
        verbose_name = 'Τιμολόγηση'
        verbose_name_plural = 'Τιμολόγηση'
        ordering = ['id']
   
    
    