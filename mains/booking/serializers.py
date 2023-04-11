from .models import Booking
from users.models import Passenger
from core.serializers import BaseSerializer
from users.serializers import PassengerSerializer

class BookingSerializer(BaseSerializer):
    passenger = PassengerSerializer(many=True)

    class Meta:
        model = Booking
        fields = '__all__'


    # decreasing airline_seats by no. of passenger
    def validate(self, attrs):
        flight_instance = attrs.get('flight')  
        passengers_data = attrs.get('passenger')
        count = len(passengers_data)

        if flight_instance.airline_seats >= count:
            attrs['status'] = 2
            flight_instance.airline_seats -= count
        else:
            attrs['status'] = 3

        flight_instance.save()
        return attrs


    # for getting serialized passenger instead of using it's pk value
    def create(self, validated_data):
        passengers_data = validated_data.pop('passenger')
        booking = Booking.objects.create(**validated_data)

        for passenger_data in passengers_data:
            passenger = Passenger.objects.create(**passenger_data)
            booking.passenger.add(passenger)

        return booking