from django.db import models

# Create your models here.
class Schools(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

class Country(models.Model):
    name = models.CharField(max_length=200)

    
