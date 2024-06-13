from django.contrib import admin

# Register your models here.
from .models import Rental, Image

admin.site.register(Rental)
admin.site.register(Image)
