# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from importlib import reload
from django.db.models import Sum
from django.contrib.auth.models import User
# from django.db.models.signals import post_save
from django.dispatch import receiver

import datetime

type_choice = (
    ('laptop', 'Laptop'),
    ('desktop', 'Desktop'),
    ('tameiakh', 'Ταμειακή Μηχανή'),

)

tmhma_choice = (
    ('1', 'Οικονομική'),
    ('2', 'Τεχνική'),
    ('3', 'Διοικητική'),
    ('4', 'Γραφείο Προσωπικού'),
    ('5', 'Μισθοδοσία'),
    ('6', 'Γραφείο Δημάρχου'),
    ('7', 'Τμήμα Πληροφορικής'),
    ('8', 'Ληξιαρχείο'),
    ('9', 'Αντιδήμαρχος'),
    ('10', 'Γραφείο Κίνησης')

)

job_choice = (
    ('TeamViewer', 'TeamViewer'),
    ('Επίσκεψη', 'Επίσκεψη'),
    ('Γραφείο', 'Γραφείο')
)

adeia_choice = (
    ('1', 'Κανονική'),
    ('2', 'Αναρρωτική'),
    ('3', 'Εορταστική')
)

app_choice = (
    ('ΤΑΠ', 'ΤΑΠ'),
    ('Μισθοδοσία', 'Μισθοδοσία'),
    ('Διαχείριση Προσωπικού', 'Διαχείριση Προσωπικού'),
    ('Λογιστική', 'Λογιστική'),
    ('Μητρώο Πολιτών', 'Μητρώο Πολιτών'),
    ('Ύδρευση', 'Ύδρευση'),
    ('Αποφάσεις', 'Αποφάσεις'),
    ('Πρωτόκολλο', 'Πρωτόκολλο'),
    ('Γραφείο Κίνησης', 'Γραφείο Κίνησης'),
    ('Διαύγεια', 'Διαύγεια'),
    ('Έσοδα', 'Έσοδα'),
    ('Κοιμητήρια', 'Κοιμητήρια'),
    ('ΚΟΚ', 'ΚΟΚ'),
    ('Δημοτικός φόρος', 'Δημοτικός φόρος'),
    ('Site', 'Site'),
    ('Πρακτικό', 'Πρακτικό'),
    ('Hardware', 'Hardware')
)

pc_brand_choice = (
    ('HP', 'HP'),
    ('Fujitsu', 'Fujitsu'),
    ('Acer', 'Acer'),
    ('Lenovo', 'Lenovo'),
    ('Custom', 'Custom')
)

polisi_choice = (
    ('OPEN', 'OPEN'),
    ('CLOSED', 'CLOSED')
)


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
        ordering = ['id']

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
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Κόστος', null=False, blank=False)
    year = models.CharField(max_length=50, verbose_name='Έτος', null=False, blank=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Service'

    def __str__(self):
        return self.customername


class Ergasies(models.Model):
    dhmos = models.ForeignKey('Dhmos', on_delete=models.CASCADE, verbose_name='Πελάτης', default='-')
    importdate = models.DateField(default=datetime.date.today, verbose_name='Ημ. Κατ.')
    app = models.CharField(max_length=100, choices=app_choice,verbose_name='Εφαρμογή', blank=True)
    jobtype = models.CharField(max_length=100, choices=job_choice,verbose_name='Τύπος Εργασίας', default='TeamViewer')
    info = models.TextField(max_length=1000, verbose_name='Περιγραφή')
    text = models.TextField(max_length=1000, verbose_name='Σημειώσεις', blank=True)
    employee = models.ForeignKey('auth.User', max_length=100, verbose_name='Υπάλληλος', on_delete=models.CASCADE,default='-')  # delete kai
    time = models.CharField(max_length=20, verbose_name='Διάρκεια', default=0)
    name = models.CharField(max_length=100, verbose_name='Υπάλληλος Επικοιν.', null=True, help_text='Επώνυμο-Όνομα',blank=True)
    ticketid = models.CharField(max_length=50, verbose_name='Αίτημα OTS', blank=True)

    class Meta:
        verbose_name = 'Εργασίες'
        verbose_name_plural = 'Εργασίες'
        ordering = ['importdate']


class Aithmata(models.Model):
    dhmos = models.ForeignKey('Dhmos', on_delete=models.CASCADE, verbose_name='Πελάτης')
    importdate = models.DateField(default=datetime.date.today, verbose_name='Ημ. Καταχώρησης')
    info = models.TextField(max_length=500, verbose_name='Περιγραφή')
    employee = models.CharField(max_length=100, verbose_name='Όν. Υπαλλήλου')
    assign = models.ForeignKey('auth.User', max_length=100, verbose_name='Χρέωση', on_delete=models.CASCADE)
    closedate = models.DateField(verbose_name='Ημ. Κλεισίματος', blank=True, null=True)

    class Meta:
        verbose_name = 'Αιτήματα'
        verbose_name_plural = 'Αιτήματα'


class Adeia(models.Model):
    employee = models.ForeignKey('auth.User', max_length=100, verbose_name='Υπάλληλος', on_delete=models.CASCADE)
    adeiatype = models.CharField(max_length=50, choices=adeia_choice, verbose_name='Τύπος Άδειας', blank=True,default='-')
    startdate = models.DateField(default=datetime.date.today, verbose_name='Από')
    enddate = models.DateField(default=datetime.date.today, verbose_name='Έως')
    createddate = models.DateField(default=datetime.date.today, verbose_name='Ημ. Δημουργίας')
    days = models.IntegerField(verbose_name='Ημέρες', null=False, blank=False, default='0')

    class Meta:
        verbose_name = 'Άδειες'
        verbose_name_plural = 'Άδειες'

    def total(self):
        today = datetime.date.today()
        return self.__class__.objects.all().filter(createddate__year=today.year, employee=self.employee).aggregate(
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
    sinoltimi = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Συνολική τιμή', null=False,blank=False, default='0')
    katagrafi = models.DateField(default=datetime.date.today, verbose_name='Καταγραφή')
    etos = models.PositiveIntegerField(default=current_year(), verbose_name='Έτος')
    status = models.CharField(max_length=50, verbose_name='Status', null=False, blank=False, choices=polisi_choice,default='OPEN')

    class Meta:
        verbose_name = 'Πωλήσεις'
        verbose_name_plural = 'Πωλήσεις'


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Upload(models.Model):
    user = models.ForeignKey('auth.User', verbose_name='Όνομα', on_delete=models.CASCADE)
    dhmos = models.ForeignKey('Dhmos', on_delete=models.CASCADE, verbose_name='Δήμος', null=True)
    description = models.CharField(max_length=255, blank=True, verbose_name='Περιγραφή')
    file = models.FileField(upload_to=user_directory_path, default='-')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    days_sum = models.IntegerField(verbose_name="Σύνολο άδειας έτους", null=False, blank=False, default='0')
    days_left = models.IntegerField(verbose_name="Υπόλοιπο προηγούμενου έτους", null=False, blank=False, default='0')

    class Meta:
        verbose_name = 'Προφίλ χρήστη'
        verbose_name_plural = 'Προφίλ χρήστη'

    def __str__(self):
        return str(self.user)

    def total(self):
        return self.days_sum + self.days_left
