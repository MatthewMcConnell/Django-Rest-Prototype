from django.db import models

# Create your models here.

class Location (models.Model):
    name = models.CharField(max_length=128, primary_key=True)
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__ (self):
        return self.name

