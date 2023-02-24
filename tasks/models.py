from django.db import models

# Create your models here.
class User(models.Model):  #inherit Model from models class
    title = models.CharField(max_length=70)
   # email = models.EmailField(max_length=50)
    description = models.CharField(max_length=500, blank=True)

