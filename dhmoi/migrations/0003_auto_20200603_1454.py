# Generated by Django 3.0.3 on 2020-06-03 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dhmoi', '0002_auto_20200603_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ergasies',
            name='symbasi',
        ),
        migrations.AddField(
            model_name='ergasies',
            name='symbasi',
            field=models.ManyToManyField(blank=True, null=True, to='dhmoi.Symbasi'),
        ),
    ]
