# Generated by Django 4.2.11 on 2024-06-22 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0004_building_city_alter_building_area_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='lat',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='building',
            name='lon',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=10),
        ),
    ]
