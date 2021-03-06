# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from importlib import reload
from django.db.models import Sum
from django.contrib.auth.models import User
# from django.db.models.signals import post_save
from django.dispatch import receiver
from .model_choices import *

import datetime



def current_year():
    return datetime.date.today().year


class Dhmos(models.Model):
    name = models.CharField(max_length=100, verbose_name='Πελάτης', blank=False)
    address = models.CharField(max_length=100, verbose_name='Διεύθυνση', blank=True, default='-')
    city = models.CharField(max_length=100, verbose_name='Πόλη', blank=True, default='-')
    phone = models.CharField(max_length=100, verbose_name='Τηλέφωνο', blank=False)
    fax = models.CharField(max_length=50, verbose_name='Fax', blank=True)
    teamviewer = models.CharField(max_length=60, verbose_name='TeamViewer', blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(max_length=250, blank=True, null=True)
    info = models.TextField(max_length=1000, verbose_name='Πληροφορίες', blank=True)
    is_visible = models.BooleanField(default=False, verbose_name='Κατάσταση')

    class Meta:
        verbose_name = 'Πελάτες'
        verbose_name_plural = 'Πελάτες'
        ordering = ['name']

    def __str__(self):
        return self.name


class Employee(models.Model):
    dhmos = models.ForeignKey('Dhmos', on_delete=models.CASCADE, verbose_name='Πελάτης', null=True)
    firstname = models.CharField(max_length=150, verbose_name='Όνομα', null=True)
    lastname = models.CharField(max_length=150, verbose_name='Επώνυμο', null=True)
    tmhma = models.CharField(max_length=100, choices=tmhma_choice, verbose_name='Υπηρεσία', blank=True)
    phone = models.CharField(max_length=100, verbose_name='Τηλέφωνο', blank=False)
    cellphone = models.CharField(max_length=30, verbose_name='Κινητό', blank=True)
    email = models.EmailField(blank=True)
    info = models.TextField(max_length=1000, verbose_name='Πληροφορίες', blank=True)
    is_visible = models.BooleanField(default=False, verbose_name='Κατάσταση')

    class Meta:
        verbose_name = 'Στοιχεία Επικοινωνίας Πελατών'
        verbose_name_plural = 'Στοιχεία Επικοινωνίας Πελατών'

    def __str__(self):
        return (self.lastname) + " " + (self.firstname)


class Service(models.Model):
    employee = models.ForeignKey('auth.User', verbose_name='Χρήστης', on_delete=models.CASCADE)
    customername = models.CharField(max_length=150, verbose_name='Ονομα Πελάτη', null=False, blank=True)  # first last
    phone = models.CharField(max_length=100, verbose_name='Τηλέφωνο Σταθερό', null=True, blank=True)
    cellphone = models.CharField(max_length=100, verbose_name='Κινητό Τηλέφωνο', null=True, blank=True)
    modelinfo = models.CharField(max_length=150, choices=type_choice, verbose_name='Τύπος', null=True, blank=True)
    serialnumber = models.CharField(max_length=100, verbose_name='S/N', null=True, blank=True)
    modeltype = models.CharField(max_length=150, verbose_name='Μοντέλο', null=True, blank=True)
    importdate = models.DateField(default=datetime.date.today, verbose_name='Καταγραφή')
    info = models.TextField(max_length=500, verbose_name='Διάγνωση', null=True, blank=True)
    exportdate = models.DateField(default=datetime.date.today, verbose_name='Παράδοση')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Κόστος')
    year = models.CharField(max_length=50, verbose_name='Έτος', null=False, blank=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Service'

    def __str__(self):
        return self.customername


class Ergasies(models.Model):
    dhmos = models.ForeignKey('Dhmos', on_delete=models.CASCADE, verbose_name='Πελάτης', default='-')
    importdate = models.DateField(default=datetime.date.today, verbose_name='Ημ. Κατ.',db_index=True)
    app = models.CharField(max_length=100, choices=app_choice,verbose_name='Εφαρμογή', blank=True)
    jobtype = models.CharField(max_length=100, choices=job_choice,verbose_name='Τύπος Εργασίας', default='TeamViewer')
    info = models.TextField(max_length=1000, verbose_name='Περιγραφή')
    text = models.TextField(max_length=1000, verbose_name='Σημειώσεις', blank=True)
    employee = models.ForeignKey('auth.User', max_length=100, verbose_name='Υπάλληλος',on_delete=models.CASCADE, default='-')  # delete kai
    time = models.FloatField(verbose_name='Διάρκεια')
    name = models.CharField(max_length=100, verbose_name='Υπάλληλος Επικοιν.',null=True, help_text='Επώνυμο-Όνομα', blank=True)
    ticketid = models.CharField(max_length=50, verbose_name='Αίτημα OTS', blank=True)

    class Meta:
        verbose_name = 'Εργασίες'
        verbose_name_plural = 'Εργασίες'
        ordering = ['importdate']

    def get_symbasi(self):
        return ",".join([str(p) for p in self.symbasi.all()])


class Aithmata(models.Model):
    dhmos = models.ForeignKey('Dhmos', on_delete=models.CASCADE, verbose_name='Πελάτης')
    importdate = models.DateField(default=datetime.date.today, verbose_name='Ημ. Καταχώρησης')
    info = models.TextField(max_length=500, verbose_name='Περιγραφή')
    employee = models.CharField(max_length=100, verbose_name='Όν. Υπαλλήλου')
    assign = models.ForeignKey('auth.User', max_length=100, verbose_name='Χρέωση - ACS', on_delete=models.CASCADE)
    closedate = models.DateField(verbose_name='Ημ. Κλεισίματος', blank=True, null=True)
    phone = models.CharField(max_length=100, verbose_name='Τηλ. επικοινωνίας', blank=True, null=True)

    class Meta:
        verbose_name = 'Αιτήματα'
        verbose_name_plural = 'Αιτήματα'


class Adeia(models.Model):
    employee = models.ForeignKey('auth.User', max_length=100, verbose_name='Υπάλληλος', on_delete=models.CASCADE)
    adeiatype = models.CharField(max_length=50, choices=adeia_choice, verbose_name='Τύπος Άδειας', blank=True, default='-')
    startdate = models.DateField(default=datetime.date.today, verbose_name='Από')
    enddate = models.DateField(default=datetime.date.today, verbose_name='Έως')
    createddate = models.DateField(default=datetime.date.today, verbose_name='Ημ. Δημουργίας')
    days = models.IntegerField(verbose_name='Ημέρες', null=False, blank=False, default='0')

    class Meta:
        verbose_name = 'Άδειες'
        verbose_name_plural = 'Άδειες'

    def total(self):  # Προσθέτει τις μέρες άδειας του τρέχοντος έτους
        today = datetime.date.today()
        return self.__class__.objects.all().filter(createddate__year=today.year, employee=self.employee).exclude(adeiatype='2').aggregate(
            sum_all=Sum('days')).get('sum_all')


    def anarotiki_total(self): 
        today = datetime.date.today()
        return self.__class__.objects.all().filter(createddate__year=today.year, employee=self.employee, adeiatype='2').aggregate(
            sum_all=Sum('days')).get('sum_all')


    def kanoniki_total(self): 
        today = datetime.date.today()
        return self.__class__.objects.all().filter(createddate__year=today.year, employee=self.employee, adeiatype='1').aggregate(
            sum_all=Sum('days')).get('sum_all')

class Hardware(models.Model):
    employee = models.ForeignKey('auth.User', max_length=100, verbose_name='Υπάλληλος', on_delete=models.CASCADE)
    pcbrand = models.CharField(max_length=150, choices=pc_brand_choice,verbose_name='Μάρκα Η/Υ', null=True, blank=True)
    cpu = models.CharField(max_length=100, verbose_name='CPU', null=True, blank=True)
    ram = models.CharField(max_length=100, verbose_name='RAM', null=True, blank=True)
    hdd = models.CharField(max_length=100, verbose_name='HDD', null=True, blank=True)
    monitor = models.CharField(max_length=100, verbose_name='Monitor', null=True, blank=True)
    windows = models.CharField(max_length=100, verbose_name='Windows', null=True, blank=True)
    office = models.CharField(max_length=100, verbose_name='Office', null=True, blank=True)
    printer = models.CharField(max_length=100, verbose_name='Printer', null=True, blank=True)

    class Meta:
        verbose_name = 'Hardware υπαλλήλων γραφείου'
        verbose_name_plural = 'Hardware υπαλλήλων γραφείου'


class Polisi(models.Model):
    dhmos = models.ForeignKey('Dhmos', on_delete=models.CASCADE, verbose_name='Πελάτης', null=False)
    eidos = models.CharField(max_length=150, verbose_name='Είδος', null=False, blank=False)
    posothta = models.IntegerField(verbose_name='Ποσότητα', null=False, blank=False)
    sinoltimi = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Συνολική τιμή', null=False, blank=False, default='0')
    katagrafi = models.DateField(default=datetime.date.today, verbose_name='Καταγραφή')
    etos = models.PositiveIntegerField(default=current_year(), verbose_name='Έτος')
    status = models.CharField(max_length=50, verbose_name='Status',null=False, blank=False, choices=polisi_choice, default='OPEN')

    class Meta:
        verbose_name = 'Πωλήσεις'
        verbose_name_plural = 'Πωλήσεις'


class Training(models.Model):
    foreas = models.CharField(max_length=100, choices=foreas_choice, verbose_name='Φορέας', default='OTS')
    place = models.CharField(max_length=100, choices=training_place, verbose_name='Χώρος', default='-')
    importdate = models.DateField(default=datetime.date.today, verbose_name='Καταχώρηση')
    training_type = models.CharField(max_length=100, choices=training_choice, verbose_name='Εκαπίδευση', blank=False, default='Εκπαίδευση')
    app = models.CharField(max_length=100, choices=app_choice,verbose_name='Εφαρμογή', blank=True)
    time = models.FloatField(verbose_name='Διάρκεια')
    employee = models.ForeignKey('auth.User', max_length=100, verbose_name='Υπάλληλος', on_delete=models.CASCADE)
    info = models.TextField(max_length=500, verbose_name='Περιγραφή ', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Εκπαιδεύσεις'
        verbose_name_plural = 'Εκπαιδεύσεις'
        

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    days_sum = models.IntegerField(verbose_name="Σύνολο άδειας έτους", null=False, blank=False, default='0')
    days_left = models.IntegerField(verbose_name="Υπόλοιπο προηγούμενου έτους", null=False, blank=False, default='0')

    class Meta:
        verbose_name = 'Προφίλ χρήστη'
        verbose_name_plural = 'Προφίλ χρήστη'

    def __str__(self):
        return str(self.user)

    def total(self):  # Προσθέτει τον αριθμό ημερώ άδειας που διακιούται ο εγαζόμενος με το υπόλοιπο μερών άδειας του προηγούμενου έτους
        return self.days_sum + self.days_left


class Tameiaki(models.Model):
    brand_name = models.CharField(max_length=200, verbose_name="Επωνυμία", null=False, blank=False)
    business = models.CharField(max_length=200, verbose_name="Επιχείρηση", null=False, blank=False)
    afm = models.CharField(max_length=200, verbose_name="Α.Φ.Μ", null=False, blank=False)
    address = models.CharField(max_length=200, verbose_name="Διεύθυνση", null=False, blank=False)
    phone = models.CharField(max_length=50, verbose_name="Τηλέφωνο", null=False, blank=False)
    cash_model = models.CharField(max_length=150, choices=cash_model, verbose_name='Μοντέλο Ταμ.', null=True, blank=True)
    old_os_version = models.CharField(max_length=50, verbose_name="Τρέχον έκδοση λογισμικού", null=True, blank=True)
    new_os_version = models.CharField(max_length=50, verbose_name="Νέα έκδοση λογισμικού", null=True, blank=True)
    cash_register_number = models.CharField(max_length=100, verbose_name="Αρ. Μητρώου Ταμειακής", null=True, blank=True)
    submission_date = models.DateField(verbose_name="Ημερομηνία Υποβολής TAXIS",auto_now_add=True)
    status = models.CharField(max_length=150, choices=tameiaki_status_choice, verbose_name='Κατάσταση', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Ταμειακές'
        verbose_name_plural = 'Ταμειακές'


