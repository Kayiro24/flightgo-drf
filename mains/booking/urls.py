from django.urls import re_path, include
from .views import BookingsViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register('', BookingsViewSet, "booking")


urlpatterns = [
    re_path('', include(router.urls)),
]