from rest_framework import mixins
from rest_framework import viewsets
from .models import User, Passenger
from .serializers import UserSerializer, PassengerSerializer


# Create your views here.
class RegisterUser(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterPassenger(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer