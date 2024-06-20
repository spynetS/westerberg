from django.db import models

# Create your models here.
class ServiceReport(models.Model):
    name        =  models.TextField("")
    email       =  models.EmailField("")
    phone       =  models.TextField("")
    adress      =  models.TextField("")
    postnumber  =  models.IntegerField()
    area        =  models.TextField("")
    homedate    =  models.DateField()
    homefrom    =  models.TimeField()
    hometo      =  models.TimeField()
    description =  models.TextField("")
