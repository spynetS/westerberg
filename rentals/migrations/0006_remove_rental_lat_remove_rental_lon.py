# Generated by Django 4.2.11 on 2024-06-22 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0005_rental_lokal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rental',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='rental',
            name='lon',
        ),
    ]
