# Generated by Django 3.0.3 on 2020-09-02 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dhmoi', '0004_tameiaki'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dhmos',
            options={'ordering': ['name'], 'verbose_name': 'Πελάτες', 'verbose_name_plural': 'Πελάτες'},
        ),
    ]
