# Generated by Django 4.2.1 on 2023-05-22 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_country_flag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='flag',
        ),
    ]
