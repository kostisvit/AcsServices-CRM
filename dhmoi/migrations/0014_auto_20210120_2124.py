# Generated by Django 3.0.7 on 2021-01-20 19:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dhmoi', '0013_auto_20210102_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ergasies',
            name='importdate',
            field=models.DateField(db_index=True, default=datetime.date.today, verbose_name='Ημ. Κατ.'),
        ),
    ]
