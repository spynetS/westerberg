from django.conf import empty
from django.db import models
from django.template.defaultfilters import default, slugify
# Create your models here.
class Images(models.Model):
    image = models.ImageField()
    def __str__(self):
            return self.image.name

class Building(models.Model):

    class City(models.TextChoices):
        NORRKOPING  = "1", "Norrköping"
        SODERKOPING = "2", "Söderköping"
        ABY         = "3", "Åby"


    class Area(models.TextChoices):
        KNEIPPEN    = "1", "Kneippen/Skarphagen"
        NORDANTILL  = "2", "Nordantill"
        OSTANTILL   = "3", "Östantill"
        SODER       = "4", "Söder"
        SODERKOPING = "5", "Söderköping"
        ABY         = "6", "Åby"

    @classmethod
    def get_city_list(cls):
        return [(choice.value, choice.label) for choice in cls.City]

    @classmethod
    def get_area_list(cls):
        return [(choice.value, choice.label) for choice in cls.Area]

    area        = models.CharField(max_length=2,choices=Area.choices)
    city        = models.CharField(max_length=2,choices=City.choices, default=City.NORRKOPING)
    adress      = models.TextField()

    lon = models.DecimalField(max_digits=10,decimal_places=6,default=0)
    lat = models.DecimalField(max_digits=10,decimal_places=6,default=0)

    description = models.TextField()
    images      = models.ManyToManyField(to=Images, related_name='images', blank=True)

    def __str__(self):
        return self.adress
