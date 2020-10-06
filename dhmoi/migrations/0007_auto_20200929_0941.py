# Generated by Django 3.0.3 on 2020-09-29 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dhmoi', '0006_auto_20200911_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ergasies',
            name='app',
            field=models.CharField(blank=True, choices=[('ΤΑΠ', 'ΤΑΠ'), ('Μισθοδοσία', 'Μισθοδοσία'), ('Διαχείριση Προσωπικού', 'Διαχείριση Προσωπικού'), ('Διαχείριση Μισθωμάτων', 'Διαχείριση Μισθωμάτων'), ('Λογιστική', 'Λογιστική'), ('Μητρώο Πολιτών', 'Μητρώο Πολιτών'), ('Ύδρευση', 'Ύδρευση'), ('Αποφάσεις', 'Αποφάσεις'), ('Πρωτόκολλο', 'Πρωτόκολλο'), ('Γραφείο Κίνησης', 'Γραφείο Κίνησης'), ('Διαύγεια', 'Διαύγεια'), ('Έσοδα', 'Έσοδα'), ('Κοιμητήρια', 'Κοιμητήρια'), ('ΚΟΚ', 'ΚΟΚ'), ('Δημοτικός φόρος', 'Δημοτικός φόρος'), ('Site', 'Site'), ('Πρακτικό', 'Πρακτικό'), ('Hardware', 'Hardware'), ('Ύδατα', 'Ύδατα'), ('OPEN1 Process', 'OPEN1 Process'), ('OPEN1 Fin', 'OPEN1 Fin'), ('OPEN1 HR', 'OPEN1 HR'), ('OPEN1 PROPERTY', 'OPEN1 PROPERTY'), ('4myCity', '4myCity'), ('OPEN1 Fleet', 'OPEN1 Fleet'), ('Easy Pay', 'EasyPay'), ('Εσωτερικός Έλεγχος-Επιχ. Συν.', 'Εσωτερικός Έλεγχος-Επιχ. Συν.'), ('Ηλεκτ.Εισπρ. ΔΙΑΣ', 'Ηλεκτ.Εισπρ. ΔΙΑΣ'), ('Διαχείριση Ποιότητας - ISO', 'Διαχείριση Ποιότητας - ISO')], max_length=100, verbose_name='Εφαρμογή'),
        ),
        migrations.AlterField(
            model_name='training',
            name='app',
            field=models.CharField(blank=True, choices=[('ΤΑΠ', 'ΤΑΠ'), ('Μισθοδοσία', 'Μισθοδοσία'), ('Διαχείριση Προσωπικού', 'Διαχείριση Προσωπικού'), ('Διαχείριση Μισθωμάτων', 'Διαχείριση Μισθωμάτων'), ('Λογιστική', 'Λογιστική'), ('Μητρώο Πολιτών', 'Μητρώο Πολιτών'), ('Ύδρευση', 'Ύδρευση'), ('Αποφάσεις', 'Αποφάσεις'), ('Πρωτόκολλο', 'Πρωτόκολλο'), ('Γραφείο Κίνησης', 'Γραφείο Κίνησης'), ('Διαύγεια', 'Διαύγεια'), ('Έσοδα', 'Έσοδα'), ('Κοιμητήρια', 'Κοιμητήρια'), ('ΚΟΚ', 'ΚΟΚ'), ('Δημοτικός φόρος', 'Δημοτικός φόρος'), ('Site', 'Site'), ('Πρακτικό', 'Πρακτικό'), ('Hardware', 'Hardware'), ('Ύδατα', 'Ύδατα'), ('OPEN1 Process', 'OPEN1 Process'), ('OPEN1 Fin', 'OPEN1 Fin'), ('OPEN1 HR', 'OPEN1 HR'), ('OPEN1 PROPERTY', 'OPEN1 PROPERTY'), ('4myCity', '4myCity'), ('OPEN1 Fleet', 'OPEN1 Fleet'), ('Easy Pay', 'EasyPay'), ('Εσωτερικός Έλεγχος-Επιχ. Συν.', 'Εσωτερικός Έλεγχος-Επιχ. Συν.'), ('Ηλεκτ.Εισπρ. ΔΙΑΣ', 'Ηλεκτ.Εισπρ. ΔΙΑΣ'), ('Διαχείριση Ποιότητας - ISO', 'Διαχείριση Ποιότητας - ISO')], max_length=100, verbose_name='Εφαρμογή'),
        ),
    ]