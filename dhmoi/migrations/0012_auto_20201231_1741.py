# Generated by Django 3.0.7 on 2020-12-31 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dhmoi', '0011_auto_20201231_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ergasies',
            name='time',
            field=models.FloatField(verbose_name='Διάρκεια'),
        ),
    ]