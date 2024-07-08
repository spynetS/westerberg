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

    class LokalType(models.TextChoices):
        BUTIK           = "1", "Butik"
        KONTOR          = "2", "Kontor"
        KONTORSHOTELL   = "3", "Kontorshotell"
        LAGER           = "4", "Lager/Föråd"
        P_PLATS         = "5", "P-plats/Garage"
        OVRIGT          = "6", "Övrigt"

    @classmethod
    def get_lokaltype_list(cls):
        return [(choice.value, choice.label) for choice in cls.LokalType]

    lokal = models.BooleanField(default=False)
    lokal_type = models.CharField(max_length=2,choices=LokalType.choices,default=LokalType.LAGER)

    available_from = models.DateField()

    public = models.BooleanField(default=True)
