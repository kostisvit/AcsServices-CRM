# Generated by Django 3.0.3 on 2020-03-27 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dhmoi', '0004_dhmos_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='ergasies',
            name='is_visible',
            field=models.BooleanField(default=False, verbose_name='!'),
        ),
    ]