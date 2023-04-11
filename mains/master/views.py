from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from .models import Aircraft, Airport
from .serializers import AircraftSerializer, AirportSerializer


class AircraftSetViewList(mixins.ListModelMixin, GenericViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer


class AirportSetViewList(mixins.ListModelMixin, GenericViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer