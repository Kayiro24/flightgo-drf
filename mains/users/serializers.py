from core.serializers import BaseSerializer
from .models import User, Passenger


class UserSerializer(BaseSerializer):
    class Meta:
        model = User
        exclude = ["last_login", "is_superuser", "last_name", "email", "is_staff", "is_active", "date_joined", "groups", "user_permissions"]


class PassengerSerializer(BaseSerializer):
    class Meta:
        model = Passenger
        exclude = ["id", "last_login", "is_superuser", "last_name", "email", "is_staff", "is_active", "date_joined", "groups", "user_permissions"]