from django.contrib.auth.models import AbstractUser
from django.db import models

from buildings.models import Images

class CustomUser(AbstractUser):
    phonenumber = models.TextField(default="")
    mobilenumber = models.TextField(default="")

    profile_picture = models.ForeignKey(Images,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.username
