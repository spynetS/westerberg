from django.db import models

from buildings.models import Images

# Create your models here.
class News(models.Model):
   title = models.TextField()
   description = models.TextField()
   image = models.ImageField(upload_to="news/",null=True)

   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
