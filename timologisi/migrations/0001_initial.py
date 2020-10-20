# Generated by Django 3.0.7 on 2020-10-20 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dhmoi', '0007_auto_20200929_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prosfora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(blank=True, choices=[('ΤΑΠ', 'ΤΑΠ'), ('Μισθοδοσία', 'Μισθοδοσία'), ('Διαχείριση Προσωπικού', 'Διαχείριση Προσωπικού'), ('Διαχείριση Μισθωμάτων', 'Διαχείριση Μισθωμάτων'), ('Λογιστική', 'Λογιστική'), ('Μητρώο Πολιτών', 'Μητρώο Πολιτών'), ('Ύδρευση', 'Ύδρευση'), ('Αποφάσεις', 'Αποφάσεις'), ('Πρωτόκολλο', 'Πρωτόκολλο'), ('Γραφείο Κίνησης', 'Γραφείο Κίνησης'), ('Διαύγεια', 'Διαύγεια'), ('Έσοδα', 'Έσοδα'), ('Κοιμητήρια', 'Κοιμητήρια'), ('ΚΟΚ', 'ΚΟΚ'), ('Δημοτικός φόρος', 'Δημοτικός φόρος'), ('Site', 'Site'), ('Πρακτικό', 'Πρακτικό'), ('Hardware', 'Hardware'), ('Ύδατα', 'Ύδατα'), ('OPEN1 Process', 'OPEN1 Process'), ('OPEN1 Fin', 'OPEN1 Fin'), ('OPEN1 HR', 'OPEN1 HR'), ('OPEN1 PROPERTY', 'OPEN1 PROPERTY'), ('4myCity', '4myCity'), ('OPEN1 Fleet', 'OPEN1 Fleet'), ('Easy Pay', 'EasyPay'), ('Εσωτερικός Έλεγχος-Επιχ. Συν.', 'Εσωτερικός Έλεγχος-Επιχ. Συν.'), ('Ηλεκτ.Εισπρ. ΔΙΑΣ', 'Ηλεκτ.Εισπρ. ΔΙΑΣ'), ('Διαχείριση Ποιότητας - ISO', 'Διαχείριση Ποιότητας - ISO')], max_length=100, null=True)),
                ('poso', models.DecimalField(decimal_places=2, max_digits=6)),
                ('is_approved', models.BooleanField(default=False)),
                ('prosfora_des', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dhmoi.Employee')),
                ('pelatis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dhmoi.Dhmos')),
            ],
            options={
                'verbose_name': 'Προσφορά',
                'verbose_name_plural': 'Προσφορά',
                'ordering': ['id'],
            },
        ),
    ]
