from django.db import models

# Create your models here.

class cities(models.Model): # class to store database / tables

    City = models.CharField(max_length = 50) # for storing characters / max_length for maximum length

    def __str__(self):

        return self.City # func to return city names