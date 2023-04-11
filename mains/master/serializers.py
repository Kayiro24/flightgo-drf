from core.serializers import BaseSerializer
from .models import Aircraft, Airport


class AircraftSerializer(BaseSerializer):
    class Meta:
        model = Aircraft
        fields = '__all__'


class AirportSerializer(BaseSerializer):
    class Meta:
        model = Airport
        fields = '__all__'
