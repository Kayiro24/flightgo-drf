from .models import Flight
from core.serializers import BaseSerializer


class FlightSerializer(BaseSerializer):
    class Meta:
        model = Flight
        fields = '__all__'