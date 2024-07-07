from django.conf import empty
from django.db import models
from django.template.defaultfilters import default, slugify
from PIL import Image as PilImage
from io import BytesIO
from django.core.files.base import ContentFile
import os

# Create your models here.
class Images(models.Model):
    image = models.ImageField(upload_to='images/original/')
    thumbnail = models.ImageField(upload_to='images/thumbnail/', null=True, blank=True)
    medium = models.ImageField(upload_to='images/medium/', null=True, blank=True)

    def save(self, *args, **kwargs):
        # Call the image save method to save the image image
        super().save(*args, **kwargs)
        if self.image and not self.thumbnail:
            self.create_thumbnails()

    def create_thumbnails(self):
        img = PilImage.open(self.image)

        # Create and save thumbnail
        self.thumbnail = self.resize_image(img, (100, 100), 'thumbnail')
        self.medium = self.resize_image(img, (300, 300), 'medium')

        super().save()

    def resize_image(self, img, size, prefix):
        # Create a copy of the image to avoid modifying the image image
        img_copy = img.copy()
        img_copy.thumbnail(size, PilImage.LANCZOS)

        thumb_io = BytesIO()
        img_copy.save(thumb_io, format=img.format)

        # Create a new filename for the thumbnail/medium image
        base, ext = os.path.splitext(os.path.basename(self.image.name))
        filename = f"{base}{ext}"
        return ContentFile(thumb_io.getvalue(), filename)

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
