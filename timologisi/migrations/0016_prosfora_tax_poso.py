# Generated by Django 3.0.7 on 2021-01-20 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timologisi', '0015_auto_20210113_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='prosfora',
            name='tax_poso',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=8),
        ),
    ]
