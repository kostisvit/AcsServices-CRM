# Generated by Django 3.0.3 on 2020-03-27 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dhmoi', '0012_training_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
