# Generated by Django 3.0.7 on 2020-08-27 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20200827_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='closed',
        ),
    ]