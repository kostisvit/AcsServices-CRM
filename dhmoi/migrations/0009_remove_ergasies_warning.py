# Generated by Django 3.0.3 on 2020-03-27 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dhmoi', '0008_auto_20200327_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ergasies',
            name='warning',
        ),
    ]