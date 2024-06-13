# Generated by Django 5.0.6 on 2024-06-13 19:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('buildings', '0004_building_city_alter_building_area_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='rentals/')),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('rooms', models.IntegerField()),
                ('description', models.TextField()),
                ('rent', models.IntegerField()),
                ('fetures', models.TextField()),
                ('avalible_from', models.DateField()),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buildings.building')),
                ('images', models.ManyToManyField(blank=True, related_name='images', to='rentals.image')),
            ],
        ),
    ]
