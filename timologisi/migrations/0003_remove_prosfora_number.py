# Generated by Django 3.0.3 on 2020-10-13 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timologisi', '0002_prosfora_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prosfora',
            name='number',
        ),
    ]
