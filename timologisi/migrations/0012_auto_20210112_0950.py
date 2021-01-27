# Generated by Django 3.0.7 on 2021-01-12 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timologisi', '0011_contract_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='contract_code',
        ),
        migrations.AddField(
            model_name='invoice',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, unique=True),
        ),
    ]