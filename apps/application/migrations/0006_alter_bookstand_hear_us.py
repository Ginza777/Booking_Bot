# Generated by Django 4.2.1 on 2023-05-24 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_ticketinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookstand',
            name='hear_us',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='application.hearingus', verbose_name='Hearing us'),
        ),
    ]
