# Generated by Django 3.0.3 on 2020-04-28 16:06

import datetime
import dhmoi.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dhmos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Πελάτης')),
                ('address', models.CharField(blank=True, default='-', max_length=100, verbose_name='Διεύθυνση')),
                ('city', models.CharField(blank=True, default='-', max_length=100, verbose_name='Πόλη')),
                ('phone', models.CharField(max_length=100, verbose_name='Τηλέφωνο')),
                ('fax', models.CharField(blank=True, max_length=50, verbose_name='Fax')),
                ('teamviewer', models.CharField(blank=True, max_length=60, verbose_name='TeamViewer')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('website', models.URLField(blank=True, max_length=250, null=True)),
                ('info', models.TextField(blank=True, max_length=1000, verbose_name='Πληροφορίες')),
                ('is_visible', models.BooleanField(default=False, verbose_name='Κατάσταση')),
            ],
            options={
                'verbose_name': 'Πελάτες',
                'verbose_name_plural': 'Πελάτες',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Περιγραφή')),
                ('file', models.FileField(default='-', upload_to=dhmoi.models.user_directory_path)),
                ('dhmos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dhmoi.Dhmos', verbose_name='Δήμος')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Όνομα')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foreas', models.CharField(choices=[('OTS', 'OTS'), ('Interlei', 'Interlei'), ('ACS', 'ACS')], default='OTS', max_length=100, verbose_name='Φορέας')),
                ('place', models.CharField(choices=[('Remote', 'Remote'), ('Γραφεία OTS', 'Γραφεία OTS'), ('Γραφείο ACS', 'Γραφείο ACS')], default='-', max_length=100, verbose_name='Χώρος')),
                ('importdate', models.DateField(default=datetime.date.today, verbose_name='Καταχώρηση')),
                ('training_type', models.CharField(choices=[('Εκπαίδευση', 'Εκπαίδευση')], default='Εκπαίδευση', max_length=100, verbose_name='Εκαπίδευση')),
                ('app', models.CharField(blank=True, choices=[('ΤΑΠ', 'ΤΑΠ'), ('Μισθοδοσία', 'Μισθοδοσία'), ('Διαχείριση Προσωπικού', 'Διαχείριση Προσωπικού'), ('Διαχείριση Μισθωμάτων', 'Διαχείριση Μισθωμάτων'), ('Λογιστική', 'Λογιστική'), ('Μητρώο Πολιτών', 'Μητρώο Πολιτών'), ('Ύδρευση', 'Ύδρευση'), ('Αποφάσεις', 'Αποφάσεις'), ('Πρωτόκολλο', 'Πρωτόκολλο'), ('Γραφείο Κίνησης', 'Γραφείο Κίνησης'), ('Διαύγεια', 'Διαύγεια'), ('Έσοδα', 'Έσοδα'), ('Κοιμητήρια', 'Κοιμητήρια'), ('ΚΟΚ', 'ΚΟΚ'), ('Δημοτικός φόρος', 'Δημοτικός φόρος'), ('Site', 'Site'), ('Πρακτικό', 'Πρακτικό'), ('Hardware', 'Hardware'), ('Ύδατα', 'Ύδατα'), ('OPEN1 Process', 'OPEN1 Process'), ('OPEN1 Fin', 'OPEN1 Fin'), ('OPEN1 HR', 'OPEN1 HR'), ('4myCity', '4myCity'), ('OPEN1 Fleet', 'OPEN1 Fleet'), ('Easy Pay', 'EasyPay')], max_length=100, verbose_name='Εφαρμογή')),
                ('time', models.FloatField(verbose_name='Διάρκεια')),
                ('info', models.TextField(blank=True, max_length=500, null=True, verbose_name='Περιγραφή\xa0')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employee', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Υπάλληλος')),
            ],
            options={
                'verbose_name': 'Εκπαιδεύσεις',
                'verbose_name_plural': 'Εκπαιδεύσεις',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customername', models.CharField(blank=True, max_length=150, verbose_name='Ονομα Πελάτη')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Τηλέφωνο Σταθερό')),
                ('cellphone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Κινητό Τηλέφωνο')),
                ('modelinfo', models.CharField(blank=True, choices=[('laptop', 'Laptop'), ('desktop', 'Desktop'), ('tameiakh', 'Ταμειακή Μηχανή')], max_length=150, null=True, verbose_name='Τύπος')),
                ('serialnumber', models.CharField(blank=True, max_length=100, null=True, verbose_name='S/N')),
                ('modeltype', models.CharField(blank=True, max_length=150, null=True, verbose_name='Μοντέλο')),
                ('importdate', models.DateField(default=datetime.date.today, verbose_name='Καταγραφή')),
                ('info', models.TextField(blank=True, max_length=500, null=True, verbose_name='Διάγνωση')),
                ('exportdate', models.DateField(default=datetime.date.today, verbose_name='Παράδοση')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Κόστος')),
                ('year', models.CharField(blank=True, max_length=50, verbose_name='Έτος')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Χρήστης')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Service',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days_sum', models.IntegerField(default='0', verbose_name='Σύνολο άδειας έτους')),
                ('days_left', models.IntegerField(default='0', verbose_name='Υπόλοιπο προηγούμενου έτους')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Προφίλ χρήστη',
                'verbose_name_plural': 'Προφίλ χρήστη',
            },
        ),
        migrations.CreateModel(
            name='Polisi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eidos', models.CharField(max_length=150, verbose_name='Είδος')),
                ('posothta', models.IntegerField(verbose_name='Ποσότητα')),
                ('sinoltimi', models.DecimalField(decimal_places=2, default='0', max_digits=10, verbose_name='Συνολική τιμή')),
                ('katagrafi', models.DateField(default=datetime.date.today, verbose_name='Καταγραφή')),
                ('etos', models.PositiveIntegerField(default=2020, verbose_name='Έτος')),
                ('status', models.CharField(choices=[('OPEN', 'OPEN'), ('CLOSED', 'CLOSED')], default='OPEN', max_length=50, verbose_name='Status')),
                ('dhmos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dhmoi.Dhmos', verbose_name='Πελάτης')),
            ],
            options={
                'verbose_name': 'Πωλήσεις',
                'verbose_name_plural': 'Πωλήσεις',
            },
        ),
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pcbrand', models.CharField(blank=True, choices=[('HP', 'HP'), ('Fujitsu', 'Fujitsu'), ('Acer', 'Acer'), ('Lenovo', 'Lenovo'), ('Custom', 'Custom')], max_length=150, null=True, verbose_name='Μάρκα Η/Υ')),
                ('cpu', models.CharField(blank=True, max_length=100, null=True, verbose_name='CPU')),
                ('ram', models.CharField(blank=True, max_length=100, null=True, verbose_name='RAM')),
                ('hdd', models.CharField(blank=True, max_length=100, null=True, verbose_name='HDD')),
                ('monitor', models.CharField(blank=True, max_length=100, null=True, verbose_name='Monitor')),
                ('windows', models.CharField(blank=True, max_length=100, null=True, verbose_name='Windows')),
                ('office', models.CharField(blank=True, max_length=100, null=True, verbose_name='Office')),
                ('printer', models.CharField(blank=True, max_length=100, null=True, verbose_name='Printer')),
                ('employee', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Υπάλληλος')),
            ],
            options={
                'verbose_name': 'Hardware υπαλλήλων γραφείου',
                'verbose_name_plural': 'Hardware υπαλλήλων γραφείου',
            },
        ),
        migrations.CreateModel(
            name='Ergasies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('importdate', models.DateField(default=datetime.date.today, verbose_name='Ημ. Κατ.')),
                ('app', models.CharField(blank=True, choices=[('ΤΑΠ', 'ΤΑΠ'), ('Μισθοδοσία', 'Μισθοδοσία'), ('Διαχείριση Προσωπικού', 'Διαχείριση Προσωπικού'), ('Διαχείριση Μισθωμάτων', 'Διαχείριση Μισθωμάτων'), ('Λογιστική', 'Λογιστική'), ('Μητρώο Πολιτών', 'Μητρώο Πολιτών'), ('Ύδρευση', 'Ύδρευση'), ('Αποφάσεις', 'Αποφάσεις'), ('Πρωτόκολλο', 'Πρωτόκολλο'), ('Γραφείο Κίνησης', 'Γραφείο Κίνησης'), ('Διαύγεια', 'Διαύγεια'), ('Έσοδα', 'Έσοδα'), ('Κοιμητήρια', 'Κοιμητήρια'), ('ΚΟΚ', 'ΚΟΚ'), ('Δημοτικός φόρος', 'Δημοτικός φόρος'), ('Site', 'Site'), ('Πρακτικό', 'Πρακτικό'), ('Hardware', 'Hardware'), ('Ύδατα', 'Ύδατα'), ('OPEN1 Process', 'OPEN1 Process'), ('OPEN1 Fin', 'OPEN1 Fin'), ('OPEN1 HR', 'OPEN1 HR'), ('4myCity', '4myCity'), ('OPEN1 Fleet', 'OPEN1 Fleet'), ('Easy Pay', 'EasyPay')], max_length=100, verbose_name='Εφαρμογή')),
                ('jobtype', models.CharField(choices=[('TeamViewer', 'TeamViewer'), ('Επίσκεψη', 'Επίσκεψη'), ('Γραφείο', 'Γραφείο')], default='TeamViewer', max_length=100, verbose_name='Τύπος Εργασίας')),
                ('info', models.TextField(max_length=1000, verbose_name='Περιγραφή')),
                ('text', models.TextField(blank=True, max_length=1000, verbose_name='Σημειώσεις')),
                ('time', models.CharField(default=0, max_length=20, verbose_name='Διάρκεια')),
                ('name', models.CharField(blank=True, help_text='Επώνυμο-Όνομα', max_length=100, null=True, verbose_name='Υπάλληλος Επικοιν.')),
                ('ticketid', models.CharField(blank=True, max_length=50, verbose_name='Αίτημα OTS')),
                ('dhmos', models.ForeignKey(default='-', on_delete=django.db.models.deletion.CASCADE, to='dhmoi.Dhmos', verbose_name='Πελάτης')),
                ('employee', models.ForeignKey(default='-', max_length=100, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Υπάλληλος')),
            ],
            options={
                'verbose_name': 'Εργασίες',
                'verbose_name_plural': 'Εργασίες',
                'ordering': ['importdate'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=150, null=True, verbose_name='Όνομα')),
                ('lastname', models.CharField(max_length=150, null=True, verbose_name='Επώνυμο')),
                ('tmhma', models.CharField(blank=True, choices=[('1', 'Οικονομική'), ('2', 'Τεχνική'), ('3', 'Διοικητική'), ('4', 'Γραφείο Προσωπικού'), ('5', 'Μισθοδοσία'), ('6', 'Γραφείο Δημάρχου'), ('7', 'Τμήμα Πληροφορικής'), ('8', 'Ληξιαρχείο'), ('9', 'Αντιδήμαρχος'), ('10', 'Γραφείο Κίνησης')], max_length=100, verbose_name='Υπηρεσία')),
                ('phone', models.CharField(max_length=100, verbose_name='Τηλέφωνο')),
                ('cellphone', models.CharField(blank=True, max_length=30, verbose_name='Κινητό')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('info', models.TextField(blank=True, max_length=1000, verbose_name='Πληροφορίες')),
                ('is_visible', models.BooleanField(default=False, verbose_name='Κατάσταση')),
                ('dhmos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dhmoi.Dhmos', verbose_name='Πελάτης')),
            ],
            options={
                'verbose_name': 'Στοιχεία Επικοινωνίας Πελατών',
                'verbose_name_plural': 'Στοιχεία Επικοινωνίας Πελατών',
            },
        ),
        migrations.CreateModel(
            name='Aithmata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('importdate', models.DateField(default=datetime.date.today, verbose_name='Ημ. Καταχώρησης')),
                ('info', models.TextField(max_length=500, verbose_name='Περιγραφή')),
                ('employee', models.CharField(max_length=100, verbose_name='Όν. Υπαλλήλου')),
                ('closedate', models.DateField(blank=True, null=True, verbose_name='Ημ. Κλεισίματος')),
                ('assign', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Χρέωση')),
                ('dhmos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dhmoi.Dhmos', verbose_name='Πελάτης')),
            ],
            options={
                'verbose_name': 'Αιτήματα',
                'verbose_name_plural': 'Αιτήματα',
            },
        ),
        migrations.CreateModel(
            name='Adeia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adeiatype', models.CharField(blank=True, choices=[('1', 'Κανονική'), ('2', 'Αναρρωτική'), ('3', 'Εορταστική')], default='-', max_length=50, verbose_name='Τύπος Άδειας')),
                ('startdate', models.DateField(default=datetime.date.today, verbose_name='Από')),
                ('enddate', models.DateField(default=datetime.date.today, verbose_name='Έως')),
                ('createddate', models.DateField(default=datetime.date.today, verbose_name='Ημ. Δημουργίας')),
                ('days', models.IntegerField(default='0', verbose_name='Ημέρες')),
                ('employee', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Υπάλληλος')),
            ],
            options={
                'verbose_name': 'Άδειες',
                'verbose_name_plural': 'Άδειες',
            },
        ),
    ]
