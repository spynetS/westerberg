from django.db import models

# Create your models here.
from buildings.models import Building

class Image(models.Model):
    image = models.ImageField(upload_to="rentals/")
    def __str__(self):
            return self.image.name

class Rental(models.Model):

    building = models.ForeignKey(Building,on_delete=models.CASCADE) # adress here
    size = models.IntegerField() # kvadrat meter
    rooms = models.IntegerField() # rooms
    description = models.TextField()
    rent = models.IntegerField()
    features = models.TextField() # json list ["Diskmakin", "Tv"]
    images = models.ManyToManyField(Image,related_name="images",blank=True)

    lon = models.DecimalField(max_digits=10,decimal_places=6,default=0)
    lat = models.DecimalField(max_digits=10,decimal_places=6,default=0)


    avalible_from = models.DateField()
