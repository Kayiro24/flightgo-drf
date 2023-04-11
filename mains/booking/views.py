from .models import Booking
from .serializers import BookingSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response


# Create your views here.
class BookingsViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    # it will cancel the ticket, change waitlist to booked according to no. of seats left
    # def destroy(self, request, pk=None):
    #     booking = self.get_object()
    #     flight = booking.flight
    #     passengers = booking.passenger.all()

    #     num_passengers = len(passengers)
    #     flight.airline_seats += num_passengers

    #     users = Booking.objects.all().order_by('id')
    #     for user in users:
    #         if user.status == 3:
    #             if len(user.passenger.all()) >= user.flight.airline_seats:
    #                 user.status = 2
    #                 user.flight.airline_seats -= len(user.passenger.all())
    #                 user.save()
    #                 break

    #     flight.save()
    #     booking.delete()

    #     return Response({'message': "Ticket Cancelled"})
