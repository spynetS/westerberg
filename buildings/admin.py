from django.contrib import admin

# Register your models here.

from .models import Building, Images


admin.site.register(Building)
admin.site.register(Images)
