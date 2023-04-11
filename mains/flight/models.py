from django.db import models
from master.models import Aircraft, Airport
from datetime import date

# Create your models here.
class Flight(models.Model):
    flight_name = models.ForeignKey(Aircraft, on_delete=models.CASCADE, related_name="flightname")
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="origin")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="destination")
    airline_seats = models.IntegerField(default=1)
    
    date = models.DateField(default=date.today)
    price = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.flight_name} : {self.date} ({self.origin} - {self.destination})"