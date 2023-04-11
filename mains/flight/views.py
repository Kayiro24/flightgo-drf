from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from .models import Flight
from .serializers import FlightSerializer
from core.views import ModelPaginationViewSet


class SearchFlightViewSet(ModelPaginationViewSet, mixins.RetrieveModelMixin, GenericViewSet):
    permission_classes = [AllowAny]
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    # searching origin and destination by names on url
    search_fields = ['origin__city', 'destination__city', 'flight_name__aircraft_name', 'date']
    # __ is used for foreign key values while date is local value