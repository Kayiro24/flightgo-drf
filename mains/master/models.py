from django.db import models


# Create your models here.
class Aircraft(models.Model):
    aircraft_name = models.CharField(max_length=21)
    aircraft_code = models.CharField(max_length=7)

    def __str__(self):
        return f"{self.aircraft_name} ({self.aircraft_code})"
    

class Airport(models.Model):
    city = models.CharField(max_length=15)
    code = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.city} ({self.code})"
        