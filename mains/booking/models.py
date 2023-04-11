from django.db import models
from flight.models import Flight
from users.models import User, Passenger
from django.utils.crypto import get_random_string
import choices


# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, name="user")
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, name="flight")
    passenger = models.ManyToManyField(Passenger, name="passenger")
    status = models.PositiveSmallIntegerField(choices=choices.BOOKING_STATUS, default=1)
    booking_id = models.CharField(max_length=6, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.booking_id = get_random_string(length=6)
        super().save(*args, **kwargs)