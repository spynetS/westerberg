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
        RESTURANG       = "2", "Resturang"
        KONTOR          = "3", "Kontor"
        KONTORSHOTELL   = "4", "Kontorshotell"
        LAGER           = "5", "Lager/Föråd"
        P_PLATS         = "6", "P-plats/Garage"
        OVRIGT          = "7", "Övrigt"

    @classmethod
    def get_lokaltype_list(cls):
        return [(choice.value, choice.label) for choice in cls.LokalType]

    lokal = models.BooleanField(default=False)
    lokal_type = models.CharField(max_length=2,choices=LokalType.choices,default=LokalType.LAGER)

    available_from = models.DateField()

    public = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)  # Add this line
