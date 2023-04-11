from django.db.models.signals import post_delete
from django.dispatch import receiver
from booking.models import Booking


@receiver(post_delete, sender=Booking)
def delete_callback(sender, instance, **kwargs):
    booking = instance
    flight = booking.flight
    passengers = booking.passenger.all()

    num_passengers = len(passengers)
    flight.airline_seats += num_passengers
    users = Booking.objects.all().order_by('id')
    for user in users:
        if user.status == 3:
            if len(user.passenger.all()) >= user.flight.airline_seats:
                user.status = 2    
                booking.flight.airline_seats -= user.flight.airline_seats
                user.save()
                break

    flight.save()